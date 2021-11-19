from PyQt5 import  uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="notas"
)
def funcao_principal():
    notaav1 = trabav2.lineEdit.text()
    notaav2 = trabav2.lineEdit_2.text()
    notaav3 = trabav2.lineEdit_3.text()
    notaavd = trabav2.lineEdit_4.text()
    notaavds = trabav2.lineEdit_5.text()
    nome = trabav2.lineEdit_6.text()
    ID_matricula = trabav2.lineEdit_7.text()
    email = trabav2.lineEdit_8.text()
    endereço = trabav2.lineEdit_9.text()
    campus = trabav2.lineEdit_10.text()
    periodo = trabav2.lineEdit_11.text()
    print("av1",notaav1)
    print("av2",notaav2)
    print("av3",notaav3)
    print("avd",notaavd)
    print("avds",notaavds)
    print("nome",nome)
    print("matricula",ID_matricula)
    print("email",email)
    print("endereço",endereço)
    print("campus",campus)
    print("periodo",periodo)
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO notas (notaav1,notaav2,notaav3,notaavd,notaavds,nome,ID_matricula,email,endereço,campus,periodo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(notaav1),str(notaav2),str(notaav3),str(notaavd),str(notaavds),str(nome),str(ID_matricula),str(email),str(endereço),str(campus),str(periodo))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    trabav2.lineEdit.setText("")
    trabav2.lineEdit_2.setText("")
    trabav2.lineEdit_3.setText("")
    trabav2.lineEdit_4.text("")
    trabav2.lineEdit_5.text("")
    trabav2.lineEdit_6.text("")
    trabav2.lineEdit_7.text("")
    trabav2.lineEdit_8.text("")
    trabav2.lineEdit_9.text("")
    trabav2.lineEdit_10.text("")
    trabav2.lineEdit_11.text("")
app=QtWidgets.QApplication([])
trabav2=uic.loadUi("trabav2.ui")
trabav2.pushButton.clicked.connect(funcao_principal)
trabav2.show()
app.exec()
