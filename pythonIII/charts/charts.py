import matplotlib.pyplot as plt

def genertate_pie_chart():
    labels = ["A", "B", "C"]
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()