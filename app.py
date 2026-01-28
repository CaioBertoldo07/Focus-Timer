import tkinter as tk
from tkinter import font
import json
import os
from datetime import datetime

class FocusTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Focus Timer")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Variáveis de controle
        self.focus_time = 25 * 60 #  25 minutos em segundos
        self.break_time = 5 * 60 # 5 minutos em segundos
        self.current_time = self.focus_time
        self.is_running = False
        self.is_break_mode = False
        self.timer_id = None

        # Arquivos de dados
        self.data_file = "sessions.json"

        # Configurar interface 
        self.setup_ui()

        # Carregar sessões do dia
        self.load_today_sessions()

    def setup_ui(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Título
        title_label = tk.Label(
            main_frame,
            text="FOCUS TIMER",
            font=("Helvetica", 20, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=(0, 30))

        # Modo atual
        self.mode_label = tk.Label(
            main_frame,
            text="Foco",
            font=("Helvetica", 14),
            bg="#f0f0f0",
            fg="#666666"
        )
        self.mode_label.pack()

        # Display do timer
        self.timer_label = tk.Label(
            main_frame,
            text="25:00",
            font=("Helvetica", 72, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        self.timer_label.pack(pady=30)

        # Frame de botões
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(pady=20)

        # Botão Iniciar/Pausar
        self.start_button = tk.Button(
            button_frame,
            text="Iniciar",
            font=("Helvetica", 14, "bold"),
            bg="#27ae60",
            fg="white",
            width=12,
            height=2,
            border=0,
            cursor="hand2",
            command=self.toggle_timer
        )
        self.start_button.pack(side="left", padx=5)

        # Botão Pausa
        self.break_button = tk.Button(
            button_frame,
            text="Pausa",
            font=("Helvetica", 14, "bold"),
            bg="#3498db",
            fg="white",
            width=12,
            height=2,
            border=0,
            cursor="hand2",
            command=self.start_break
        )
        self.break_button.pack(side="left", padx=5)

        # Contador de sessões
        sessions_frame = tk.Frame(main_frame, bg="#f0f0f0")
        sessions_frame.pack(pady=(30, 0))

        tk.Label(
            sessions_frame,
            text="Sessões hoje:",
            font=("Helvetica", 12),
            bg="#f0f0f0",
            fg="#666666",
        ).pack()

        self.sessions_label = tk.Label(
            sessions_frame,
            text="0",
            font=("Helvetica", 36, "bold"),
            bg="#f0f0f0",
            fg="#27ae60"
        )
        self.sessions_label.pack()
    
    def toggle_timer(self):
        if self.is_running:
            # Pausar
            self.is_running = False
            self.start_button.config(text="Continuar", bg="#27ae60")
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
        else:
            # Iniciar/Continuar
            self.is_running = True
            self.start_button.config(text="Pausar", bg="#e74c3c")
            self.update_timer()
    
    def update_timer(self):
        if self.is_running and self.current_time > 0:
            self.current_time -= 1
            self.update_display()
            self.timer_id = self.root.after(1000, self.update_timer)
        elif self.is_running and self.current_time == 0:
            # Timer finalizado
            self.timer_finished()
    
    def update_display(self):
        minutes = self.current_time // 60
        seconds = self.current_time % 60
        self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
    
    def timer_finished(self):
        self.is_running = False

        if not self.is_break_mode:
            # Sessão de foco concluída
            self.save_session()
            self.load_today_sessions()
        
        # Resetar timer
        self.reset_timer()
        self.start_button.config(text="Iniciar", bg="#27ae60")
    
    def start_break(self):
        # Pausar timer atual se estiver rodando
        if self.is_running:
            self.is_running = False
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
        
        # Configurar modo pausa
        self.is_break_mode = True
        self.current_time = self.break_time
        self.mode_label.config(text="Pausa")
        self.update_display()
        self.start_button.config(text="Iniciar", bg="#27ae60")
    
    def reset_timer(self):
        if self.is_break_mode:
            # Voltar ao modo foco após pausa
            self.is_break_mode = False
            self.current_time = self.focus_time
            self.mode_label.config(text="Foco")
        else:
            # Resetar sessão de foco
            self.current_time = self.focus_time
        
        self.update_display()
    
    def save_session(self):
        # Criar arquivo se não existir
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump([], f)
        
        # Carregar dados existentes
        with open(self.data_file, 'r', encoding='utf-8') as f:
            try:
                sessions = json.load(f)
            except:
                sessions = []
        
        # Adicionar nova sessão
        now = datetime.now()
        session = {
            "data": now.strftime("%Y-%m-%d"),
            "horario": now.strftime("%H:%M:%S"),
            "tipo": "foco"
        }
        sessions.append(session)

        # Salvar
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(sessions, f, indent=2, ensure_ascii=False)
    
    def load_today_sessions(self):
        if not os.path.exists(self.data_file):
            self.sessions_label.config(text="0")
            return

        today = datetime.now().strftime("%Y-%m-%d")

        with open(self.data_file, 'r', encoding='utf-8') as f:
            try:
                sessions = json.load(f)
            except:
                sessions = []
        
        # Contar sessões de hoje
        today_sessions = [s for s in sessions if s.get("data") == today and s.get("tipo") == "foco"]
        count = len(today_sessions)
        self.sessions_label.config(text=str(count))

def main():
    root = tk.Tk()
    app = FocusTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
