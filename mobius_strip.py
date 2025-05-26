import numpy as np
import matplotlib.pyplot as plt

class MobiusStrip:
    def __init__(self, R=1.0, w=0.2, n=200):
        self.R = R
        self.w = w
        self.n = n
        self.u, self.v = np.meshgrid(
            np.linspace(0, 2 * np.pi, n),
            np.linspace(-w / 2, w / 2, n)
        )
        self.x, self.y, self.z = self._generate_coordinates()

    def _generate_coordinates(self):
        u = self.u
        v = self.v
        R = self.R

        x = (R + v * np.cos(u / 2)) * np.cos(u)
        y = (R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def compute_surface_area(self):
        du = 2 * np.pi / (self.n - 1)
        dv = self.w / (self.n - 1)

        Xu = np.gradient(self.x, du, axis=1)
        Yu = np.gradient(self.y, du, axis=1)
        Zu = np.gradient(self.z, du, axis=1)

        Xv = np.gradient(self.x, dv, axis=0)
        Yv = np.gradient(self.y, dv, axis=0)
        Zv = np.gradient(self.z, dv, axis=0)

        Nx = Yu * Zv - Zu * Yv
        Ny = Zu * Xv - Xu * Zv
        Nz = Xu * Yv - Yu * Xv

        dA = np.sqrt(Nx**2 + Ny**2 + Nz**2)
        surface_area = np.sum(dA) * du * dv
        return surface_area

    def compute_edge_length(self):
        edge_x = self.x[-1]
        edge_y = self.y[-1]
        edge_z = self.z[-1]

        dx = np.diff(edge_x)
        dy = np.diff(edge_y)
        dz = np.diff(edge_z)

        ds = np.sqrt(dx**2 + dy**2 + dz**2)
        edge_length = np.sum(ds)
        return edge_length

    def plot(self):
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.x, self.y, self.z, cmap='plasma', edgecolor='k', linewidth=0.2, alpha=0.9)
        ax.set_title('Möbius Strip')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    try:
        R = float(input("Enter the radius (R): "))
        w = float(input("Enter the width (w): "))
        n = int(input("Enter the resolution (n): "))

        mobius = MobiusStrip(R=R, w=w, n=n)
        area = mobius.compute_surface_area()
        edge = mobius.compute_edge_length()

        print(f"\n🧮 Surface Area ≈ {area:.4f}")
        print(f"📏 Edge Length ≈ {edge:.4f}")

        mobius.plot()

    except ValueError:
        print("❌ Please enter valid numeric values.")
import numpy as np
import matplotlib.pyplot as plt

class MobiusStrip:
    def __init__(self, R=1.0, w=0.2, n=200):
        self.R = R
        self.w = w
        self.n = n
        self.u, self.v = np.meshgrid(
            np.linspace(0, 2 * np.pi, n),
            np.linspace(-w / 2, w / 2, n)
        )
        self.x, self.y, self.z = self._generate_coordinates()

    def _generate_coordinates(self):
        u = self.u
        v = self.v
        R = self.R

        x = (R + v * np.cos(u / 2)) * np.cos(u)
        y = (R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def compute_surface_area(self):
        du = 2 * np.pi / (self.n - 1)
        dv = self.w / (self.n - 1)

        Xu = np.gradient(self.x, du, axis=1)
        Yu = np.gradient(self.y, du, axis=1)
        Zu = np.gradient(self.z, du, axis=1)

        Xv = np.gradient(self.x, dv, axis=0)
        Yv = np.gradient(self.y, dv, axis=0)
        Zv = np.gradient(self.z, dv, axis=0)

        Nx = Yu * Zv - Zu * Yv
        Ny = Zu * Xv - Xu * Zv
        Nz = Xu * Yv - Yu * Xv

        dA = np.sqrt(Nx**2 + Ny**2 + Nz**2)
        surface_area = np.sum(dA) * du * dv
        return surface_area

    def compute_edge_length(self):
        edge_x = self.x[-1]
        edge_y = self.y[-1]
        edge_z = self.z[-1]

        dx = np.diff(edge_x)
        dy = np.diff(edge_y)
        dz = np.diff(edge_z)

        ds = np.sqrt(dx**2 + dy**2 + dz**2)
        edge_length = np.sum(ds)
        return edge_length

    def plot(self):
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.x, self.y, self.z, cmap='plasma', edgecolor='k', linewidth=0.2, alpha=0.9)
        ax.set_title('Möbius Strip')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    try:
        R = float(input("Enter the radius (R): "))
        w = float(input("Enter the width (w): "))
        n = int(input("Enter the resolution (n): "))

        mobius = MobiusStrip(R=R, w=w, n=n)
        area = mobius.compute_surface_area()
        edge = mobius.compute_edge_length()

        print(f"\n🧮 Surface Area ≈ {area:.4f}")
        print(f"📏 Edge Length ≈ {edge:.4f}")

        mobius.plot()

    except ValueError:
        print("❌ Please enter valid numeric values.")
