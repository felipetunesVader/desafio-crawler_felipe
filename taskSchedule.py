import os


def agendar_tarefa():
    path_script = r"C:\Users\carol\desafio-crawler_felipe\app.py"
    nome_tarefa = "ExecutarDesafioCrawler"
    hora_execucao = "18:15"

    comando = f'schtasks /Create /SC DAILY /TN {nome_tarefa} /TR "python {path_script}" /ST {hora_execucao}'

    os.system(comando)


if __name__ == "__main__":
    agendar_tarefa()
