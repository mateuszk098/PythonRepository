if __name__ == "__main__":

    u1, u2 = 0, 0
    u3, u4 = 0, 0

    u5, u6 = 10, 20
    u7, u8 = 0, 0

    u9, u10 = 20, 0
    u11, u12 = 0, 0

    dt = 0.001

    x1 = [u1]
    y1 = [u2]

    x2 = [u5]
    y2 = [u6]

    x3 = [u9]
    y3 = [u10]

    m1, m2, m3 = 1, 5, 2

    for _ in range(100000):

        u1 += u3 * dt
        u2 += u4 * dt

        u3 += m2 * ((u5-u1) / ((u5-u1)**2 + (u6-u2)**2)**(1.5) +
                    m3 * (u9-u1) / ((u9-u1)**2 + (u10-u2)**2)**(1.5)) * dt
        u4 += m2 * ((u6-u2) / ((u5-u1)**2 + (u6-u2)**2)**(1.5) +
                    m3 * (u10-u2) / ((u9-u1)**2 + (u10-u2)**2)**(1.5)) * dt

        u5 += u7 * dt
        u6 += u8 * dt

        u7 += m1 * ((u1-u5) / ((u5-u1)**2 + (u6-u2)**2)**(1.5) +
                    m3*(u9-u5) / ((u9-u5)**2 + (u10-u6)**2)**(1.5)) * dt

        u8 += m1 * ((u2-u6) / ((u5-u1)**2 + (u6-u2)**2)**(1.5) +
                    m3*(u10-u6) / ((u9-u5)**2 + (u10-u6)**2)**(1.5)) * dt

        u9 += u10 * dt
        u10 += u11 * dt

        u11 += m1*((u1-u9) / ((u9-u1)**2 + (u10-u2)**2)**(1.5) +
                   m2*(u5-u9) / ((u9-u5)**2 + (u10-u6)**2)**(1.5)) * dt

        u12 += m1*((u2-u10) / ((u9-u1)**2 + (u10-u2)**2)**(1.5) +
                   m2*(u6-u10) / ((u9-u5)**2 + (u10-u6)**2)**(1.5)) * dt

        x1.append(u1)
        y1.append(u2)

        x2.append(u5)
        y2.append(u6)

        x3.append(u9)
        y3.append(u10)

    from matplotlib import pyplot as plt

    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.plot(x3, y3)
    plt.show()
