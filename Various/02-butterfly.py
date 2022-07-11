import matplotlib.pyplot as plt
import time

sigma, rho, beta = 10, 28, 10/3


def dx(x: float, y: float):
    return sigma * (y - x)


def dy(x: float, y: float, z: float):
    return x * (rho - z) - y


def dz(x: float, y: float, z: float):
    return x * y - beta * z


def runge_kutta(N: int, dt: float, x_0: float, y_0: float, z_0: float, x_list, y_list, z_list):

    for _ in range(N):

        x_list.append(x_0)
        y_list.append(y_0)
        z_list.append(z_0)

        K1x = dx(x_0, y_0) * dt
        K1y = dy(x_0, y_0, z_0) * dt
        K1z = dz(x_0, y_0, z_0) * dt

        K2x = dx(x_0 + 0.5 * K1x, y_0 + 0.5 * K1y) * dt
        K2y = dy(x_0 + 0.5 * K1x, y_0 + 0.5 * K1y, z_0 + 0.5 * K1z) * dt
        K2z = dz(x_0 + 0.5 * K1x, y_0 + 0.5 * K1y, z_0 + 0.5 * K1z) * dt

        K3x = dx(x_0 + 0.5 * K2x, y_0 + 0.5 * K2y) * dt
        K3y = dy(x_0 + 0.5 * K2x, y_0 + 0.5 * K2y, z_0 + 0.5 * K2z) * dt
        K3z = dz(x_0 + 0.5 * K2x, y_0 + 0.5 * K2y, z_0 + 0.5 * K2z) * dt

        K4x = dx(x_0 + K3x, y_0 + K3y) * dt
        K4y = dy(x_0 + K3x, y_0 + K3y, z_0 + K3z) * dt
        K4z = dz(x_0 + K3x, y_0 + K3y, z_0 + K3z) * dt

        x_0 += (K1x + 2 * K2x + 2 * K3x + K4x) / 6
        y_0 += (K1y + 2 * K2y + 2 * K3y + K4y) / 6
        z_0 += (K1z + 2 * K2z + 2 * K3z + K4z) / 6


def draw_plot(x_list, y_list, z_list):

    plt.figure(1)
    plt.grid(ls='--')
    plt.plot(x_list, z_list)
    plt.title("Lorenz Attractor")
    plt.xlabel("x")
    plt.ylabel("z")
    plt.show()


if __name__ == "__main__":

    x_0, y_0, z_0 = 1, 1, 25
    x_list, y_list, z_list = [], [], []
    N = 10_000
    dt = 1e-2

    start = time.time()
    runge_kutta(N, dt, x_0, y_0, z_0, x_list, y_list, z_list)
    stop = time.time()
    print("Execution time: " + str((stop - start) * 1e3) + " ms")

    draw_plot(x_list, y_list, z_list)
