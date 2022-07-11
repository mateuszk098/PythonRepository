import numpy as np
import matplotlib.pyplot as plt
import time
from numba import jit


# Function it is compiled to machine code “just-in-time”
@jit(nopython=True, fastmath=True)
def sim_loop(Psi_R, Psi_I, H_R, H_I, norm, x_mean, energy):

    for i in range(1, S + 1):

        Psi_R = Psi_R + H_I * 0.5 * tau

        H_R[1:-1] = -0.5 * (Psi_R[:-2] + Psi_R[2:] - 2 * Psi_R[1:-1]) / \
            (dx * dx) + K * (x[1:-1] - 0.5) * \
            Psi_R[1:-1] * np.sin(W * (t + i * tau))

        Psi_I = Psi_I - H_R * tau

        H_I[1:-1] = -0.5 * (Psi_I[:-2] + Psi_I[2:] - 2 * Psi_I[1:-1]) / \
            (dx * dx) + K * (x[1:-1] - 0.5) * \
            Psi_I[1:-1] * np.sin(W * (t + i * tau))

        Psi_R = Psi_R + H_I * 0.5 * tau

        if i % S_out == 0:

            k = int(i / 1000)
            norm[k] = np.sum(dx * (Psi_R * Psi_R + Psi_I * Psi_I))
            x_mean[k] = np.sum(dx * x * (Psi_R * Psi_R + Psi_I * Psi_I))
            energy[k] = np.sum(dx * (Psi_R * H_R + Psi_I * H_I))


def draw_plot(times, x_mean, energy):

    plt.style.use("bmh")

    # Tworzymy subplot
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1,
                                   sharex=True, figsize=(10, 4.5), dpi=100)

    ax1.plot(times, x_mean, color="blue", alpha=0.75,
             linewidth=0.5, label="x mean")
    ax1.set_title("Quantum particle's mean position and energy",
                  fontname="Times New Roman", fontsize=16)
    ax1.set_ylabel("Mean Position", fontname="Times New Roman")

    ax2.plot(times, energy, color="blue", alpha=0.75,
             linewidth=2.0, label="energy")
    ax2.set_xlabel("Time", fontname="Times New Roman")
    ax2.set_ylabel("Energy", fontname="Times New Roman")

    plt.show()


if __name__ == '__main__':

    start = time.time()

    # ----------------------------------------------------------------
    # Czytamy dane z pliku
    with open("parameters_py.txt", "r") as f:
        data = f.read()

    # Bierzemy jedynie wartosci
    data = data.split()
    data = data[0::2]

    # Zamieniamy typy na int albo float
    data = (int(i) if i.isdigit() else float(i) for i in data)

    # Rozpakowanie wartosci do zmiennnych
    N, n, m, omega, K, t, tau, S, S_out = data
    PI = np.pi
    W = omega * 0.01 * abs(m * m - n * n) * PI * PI * 0.5
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # Warunki poczatkowe
    # Polozenia
    x = np.linspace(0, 1, N + 1, dtype=float)

    # Rzeczywista czesc funkcji falowej
    Psi_R = np.array(np.sqrt(2) * np.sin(n * PI * x), dtype=float)
    # Urojona czesc funkcji falowej
    Psi_I = np.zeros(N + 1, dtype=float)

    # Rzeczywista czesc hamiltonianu
    H_R = np.zeros(N + 1, dtype=float)
    # Urojona czesc hamiltonianu
    H_I = np.zeros(N + 1, dtype=float)

    # Podzial odcinka [0,1] na N przedzialow
    dx = 1.0 / N

    # Dzialanie operatora hamiltona na funkcje falowa
    H_R[1:-1] = -0.5 * (Psi_R[:-2] + Psi_R[2:] - 2 * Psi_R[1:-1]) / \
        (dx * dx) + K * (x[1:-1] - 0.5) * Psi_R[1:-1] * np.sin(W * t)

    H_I[1:-1] = -0.5 * (Psi_I[:-2] + Psi_I[2:] - 2 * Psi_I[1:-1]) / \
        (dx * dx) + K * (x[1:-1] - 0.5) * Psi_I[1:-1] * np.sin(W * t)

    # Poczatkowe informacje o czastce
    norm_0 = np.sum(dx * (Psi_R * Psi_R + Psi_I * Psi_I))
    x_mean_0 = np.sum(dx * x * (Psi_R * Psi_R + Psi_I * Psi_I))
    energy_0 = np.sum(dx * (Psi_R * H_R + Psi_I * H_I))

    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # Symulacja
    # Tablice do wykresow
    k = int(S / S_out) + 1
    norm = np.empty(k, dtype=float)
    x_mean = np.empty(k, dtype=float)
    energy = np.empty(k, dtype=float)
    times = np.linspace(0, 50, k, dtype=float)

    # Zerowe elementy tablic to poczatkowe informacje
    norm[0] = norm_0
    x_mean[0] = x_mean_0
    energy[0] = energy_0

    # Petla symulacji
    sim_loop(Psi_R, Psi_I, H_R, H_I, norm, x_mean, energy)

    stop = time.time()
    print("Execution time: " + str("%.2f" % (stop - start)) + " s")
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # Wykresy
    draw_plot(times, x_mean, energy)
    # ----------------------------------------------------------------z
