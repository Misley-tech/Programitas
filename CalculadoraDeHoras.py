import pandas as pd
from datetime import datetime, timedelta

def CalculadoraHoras(file_path):
    """
    Estructura
        Lunes 23/8 10:00 a 12:00
        Miercoles 25/8 14:00 a 17:00
        Jueves 26/8 10:00 a 14:30 
    """
    df = pd.read_csv(file_path, header=None)
    Time = []
    for i in range(df.shape[0]):
        row = df.iloc[i].to_string(index=False, header=False)
        row = row.split()
        row.pop(0)
        row.pop(0)
        row.pop(1)
        time1 = datetime.strptime(row[0], "%H:%M")
        time2 = datetime.strptime(row[1], "%H:%M")  
        Time.append(time2-time1)
    
    sum=timedelta(hours=0, minutes=0)
    for t in Time:
        sum += t 
    
    with open(file_path, "a") as file:
        file.write("\n"+f'Horas totales: {sum}')

print(CalculadoraHoras('horas.txt'))