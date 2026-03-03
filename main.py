import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    salary_data = "./Salary_Data.csv"
    df = pd.read_csv(salary_data)

    numpy_array = pd.DataFrame.to_numpy(df)
    X = numpy_array[:, 0]
    y = numpy_array[:, 1]

    return X, y

def gradient_function(y_predict, y, X):
    Da = (2 / len(X)) * np.sum(X * (y_predict - y))
    Db = (2 / len(X)) * np.sum(y_predict - y)
    
    return Da, Db
    
def calculate_mse(y_predict, y):
    return np.mean((y_predict - y) ** 2)

def main():
    print("Hello from linearregressionfromscratch!")
    X, y = load_data()

    learning_rate = 0.01
    epochs = 2000

    # default linear parameters a and b
    a = 0
    b = 0

    # interactive plot
    plt.ion()
    fig, ax = plt.subplots()

    # error field
    error_text = ax.text(0.05, 0.95, '', transform=ax.transAxes, 
                         fontsize=12, verticalalignment='top', 
                         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    ax.scatter(X, y, color='blue', label='Data')

    line, = ax.plot(X, a * X + b, color='red', linewidth=2, label='Learning...')
    
    plt.title("Gradient Descent Visualisation Linear Regression")
    plt.legend()

    # learn loop gradient
    for i in range(epochs):
        # forward pass
        y_predict = a * X + b

        # calculated gradient for a and b
        Da, Db = gradient_function(y_predict, y, X)

        # error
        mse = calculate_mse(y_predict, y)

        # update a and b
        a = a - learning_rate * Da
        b = b - learning_rate * Db

        # update plot
        if i % 10 == 0:
            # set updated y
            line.set_ydata(a * X + b)

            # update error field
            error_text.set_text(f"Epoch: {i}\nMSE: {mse:.2f}")
            
            # refresh and pause
            plt.draw()
            plt.pause(0.05) 
    
    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()
