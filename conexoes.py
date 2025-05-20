import pyodbc

def carregar_assuntos():
    """Carrega todos os assuntos"""
    try:
        connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=sql_des;"
            "DATABASE=des_net2;"
            "UID=user_all;"
            "PWD=t1c0ml8r@"
        )
        cursor = connection.cursor()

        # 🔍 Buscar dados da FAQ no SQL Server
        cursor.execute(
            """SELECT numIdAssunto, strAssunto as assunto
                FROM Tb_Assunto_Pergunta_Python
            """)
        faq_data = cursor.fetchall()

        # Fechar conexão
        connection.close()

        print("\n✅ Conexão bem-sucedida ao SQL Server!\n")

        return faq_data

    except Exception as e:
        print(f"❌ Erro ao conectar ao SQL Server: {e}")
        exit()

