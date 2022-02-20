"""
Notiuni de acoperit:
variabile
assert
input
print
format in print
constante
type casting
dunder methods
built in functions
strings
imutabilitate (immutability)"""

"""

1 variabile + print
O variabila este o adresa de memorie la care putem sa stocam informatii.
O variabila va fi creeata abia in momentul in care ii dam o valoare care va defini si tipul de data al variabilei
Un tip de data este o proprietate care a arata ce fel de informatii putem sa stocam in variabila respectiva.

Reguli pentru definirea unei variabile:
-nu trebuie sa contina spatii
-nu trebuie sa fie cuvinte rezervate (class, int)
-trebuie sa fie/aiba un nume unic
-nu trebuie sa inceapa cu un numar
-trebuie sa urmeze formatul camelCase sau skake_case, de preferat ultima
-trebuie sa inceapa cu litera mica 
-numele variabilelor sunt Case sensitive"""

expected_user="Bianca" #pentrui ca textul sa fie tratat ca atare, trebuie sa fie pus intre ghilimele, altfel va fi considerat o variabila
expected_pass="abc123"

actual_user="Gabriela"
print(expected_user, actual_user)
expected_user=actual_user # aici nu am mai pus intre ghilimele pt ca am vrut sa citim valoarea din variabila actual_user si sa o asignam valoarea variabilei expected_user
print(expected_user, actual_user)
#-------------------------------------------------------------------------------

""" 
assert este o modalitate de a face validari rapide 
verifica daca o conditie care este evaluata este adevarata sau falsa
daca este adevarata, liniile de cod care urmeaza se vor executa, in caz contrar executia se va opri"""

a=1
assert a==1
print("test has passed")
#assert a==2
#print("this will return error")
expected_user="Bianca"
expected_password="abc123"
actual_password=input("introdu parola:")
#assert expected_password==actual_password
#---------------------------------------------------

""" 
input si formatting
input este o modalitate interactiva de a trimite valori de la tastatura care pot sa fie diferite la fiecare rulare
intre paranteze la input putem sa specificam textul care sa se afiseze pe ecran atunci cand se solicita un anumit input
atunci cand introduci o valoare de la tastatura la input, tipul de data implicit este string
"""

name=input("please insert your name:")
age=int(input("please insert your age:")) # aici am facut typeCasting adica am fortat ca tipul de data al inputului sa fie int
print(f"hello {name}, you have {age} years")
# print("hello" + name + "you have" + age + "years") #aici a dat eroare pt ca nu putem sa concatenam int cu string

#-------------------------------------------------------------
"""
constantele reprezinta un spatiu de memorie care nu trebuie sa fie schimbat
in Python nu exista un concept definit de constanta de aceea sunt folosite constantele doar ca si concept
pentru a defini o constanta o vom scrie cu litere mari
chiar daca este marcata ca si constanta prin scrierea cu litere mari, nu inseamna aca in python nu o putem modifica ci ca nu trebuie modificata"""
DAYS_OF_WEEK=7

#--------------------------------------------------------------
"""
Data types
Un tip de data este o proprietate care specifica ce fel de informatii putem sa stocam intr-o vabriabila
Cele mai folosite tipuri de data din python:
-int #stocheaza numere intregi
-float #stocheaza numere zecimale
-bool #stocheaza True sau False
-string # stocheaza text"""

#"int" #"+" la int inseamna adunare intre doua numere =suma
age=3
# "float"=
quantity=1234.5678
# bool
isActive=True
# String #"+" la string inseamna concatenare
name="Bianca"

# exemple cu "+"
nr1=3
nr2=5
print(nr1+nr2)
str1="Bianca"
str2="Gabriela"
print(str1+str2)

#------------------------------------------------
"""
Type Casting
Type casting inseamna fortarea unei variabile sa aibe un anumit tip de data."""

var1=33
print(type(var1))
print(type(str(var1))) # trateaza doar temporar ca un string
print(type(float(var1)))

#----------------------------------------
"""Dunder methods
-Dunder= double underscore __
O variabila poate sa fie definita de diverse categorii de acces:
public-varianta default
protected-definita de un underscore in fata numelui variabilei(ex _nume)-inseamna ca noi putem sa folosim variabila resp doar in acelasi pachet in care se afla
protected- definita de doua underscoruri in fata numelui variabilei (ex __nume) -inseamna ca nu putem folosi variabila decat in programul curent

in general nu este recomandat sa folosim dunders cand definim o variabila"""

# exemplu
if __name__=="__main__":
    print("this will not be printed in another module")
print("public instruction")
