import sys
from pattern_matching import algorithms
from pattern_matching import execution_time_gathering
import matplotlib.pyplot as plt

def graphicsAlgorithms():
    minimum_size = 10000
    maximum_size = 100000
    step = 10000
    samples_by_size = 5
    
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print("Size | Brute Force | Morris Pratt | Search with Automaton")
    for row in table:
        print(row)


    # La primera columna será el eje X
    x = [row[0] for row in table]
    # Las siguientes columnas serán los valores de Y
    y1 = [row[1][0] for row in table]
    y2 = [row[2][0] for row in table]
    y3 = [row[3][0] for row in table]

    # Crear el gráfico
    plt.plot(x, y1, label="Brute Force", color='blue')
    plt.plot(x, y2, label="Morris Pratt", color='green')
    plt.plot(x, y3, label="Search with Automaton", color='red')

    plt.title('Comparation Pattern Matching algorithms')
    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

    y1 = [row[1][1] for row in table]
    y2 = [row[2][1] for row in table]
    y3 = [row[3][1] for row in table]

    plt.plot(x, y1, label="Brute Force", color='blue')
    plt.plot(x, y2, label="Morris Pratt", color='green')
    plt.plot(x, y3, label="Search with Automaton", color='red')

    plt.title('Comparation Pattern Matching algorithms Memory Usage')
    plt.xlabel('Size')
    plt.ylabel('Memory')
    plt.legend()
    plt.show()

def graphicsMorrisPrattAutomaton():
    minimum_size = 50000
    maximum_size = 500000
    step = 50000
    samples_by_size = 5
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size, True)
    print("Size | Brute Force | Morris Pratt | Search with Automaton")
    for row in table:
        print(row)

    # La primera columna será el eje X
    x = [row[0] for row in table]
    # Las siguientes columnas serán los valores de Y
    y1 = [row[1][0] for row in table]
    y2 = [row[2][0] for row in table]

    # Crear el gráfico
    plt.plot(x, y1, label="Morris Pratt", color='blue')
    plt.plot(x, y2, label="Search with Automaton", color='green')

    plt.title('Comparation Pattern Matching algorithms')
    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

    y1 = [row[1][1] for row in table]
    y2 = [row[2][1] for row in table]

    plt.plot(x, y1, label="Morris Pratt", color='blue')
    plt.plot(x, y2, label="Search with Automaton", color='green')

    plt.title('Comparation Pattern Matching algorithms Memory Usage')
    plt.xlabel('Size')
    plt.ylabel('Memory')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    graphicsAlgorithms()
    graphicsMorrisPrattAutomaton()
