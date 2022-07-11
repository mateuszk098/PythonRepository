from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd


def function(t, a, c):
    return c * np.exp(-a*t)


if __name__ == '__main__':

    # Data with some noise - test
    # x_data = np.linspace(0, 5, 100)
    # y = function(x_data, 1, 1, 1)
    # rng = np.random.default_rng()
    # y_noise = 0.03 * rng.normal(size=x_data.size)
    # y_data = y + y_noise

    # Real data
    data = pd.read_csv('stała_czasowa.csv')
    # Masking only one period
    mask = (data['Time (s)'] > 0.000488) & (data['Time (s)'] < 0.000723)
    data = data[mask]
    x_data = data['Time (s)']
    y_data = data['Channel 1 (V)']

    # Fit for the parameters a, c of the function
    popt, pcov = curve_fit(function, x_data, y_data)

    # Plotting
    plt.style.use('bmh')
    figure(figsize=(6, 4), dpi=100)

    # Real data
    plt.plot(x_data, y_data, color='blue', label='Data', alpha=0.75)

    # Fit
    plt.plot(x_data, function(x_data, *popt), linestyle='--', color='red',
             label='Fit: c * exp(-a * t) \n a = %.1f, c = %.1f \n u(a) = %.1f, u(c) = %.1f' % tuple(np.append(popt, np.sqrt(np.diag(pcov)))))

    plt.title('Stała czasowa - Fit', fontname='Times New Roman')
    plt.xlabel('Time (s)', fontname='Times New Roman')
    plt.ylabel('Channel 1 (V)', fontname='Times New Roman')
    plt.legend()
    plt.show()
