class A {
    protected int x;
    protected int z;

    public A(int x, int z) {
        this.x = x;
        this.z = z;
    }

    public void incrementaXZ() {
        x++;
        z++;
    }

    public void incrementaZ() {
        z++;
    }
}


class B {
    protected int y;
    protected int z;

    public B(int y, int z) {
        this.y = y;
        this.z = z;
    }

    public void incrementaYZ() {
        y++;
        z++;
    }

    public void incrementaZ() {
        z++;
    }
}

class D {
    private A a;
    private B b;

    public D(int x, int y, int z) {
        a = new A(x, z);
        b = new B(y, z);
    }

    public void incrementaXYZ() {
        a.x++;
        b.y++;
        a.z++;
    }

    public void incrementaXZ() {
        a.incrementaXZ();
    }

    public void incrementaYZ() {
        b.incrementaYZ();
    }

    public void incrementaZ() {
        a.incrementaZ();
    }

    public int getX() {
        return a.x;
    }

    public int getY() {
        return b.y;
    }

    public int getZ() {
        return a.z;
    }
}

public class Main {
    public static void main(String[] args) {
        D d = new D(1, 2, 3);

        System.out.println("Valores iniciales:");
        System.out.println("x = " + d.getX());
        System.out.println("y = " + d.getY());
        System.out.println("z = " + d.getZ());

        d.incrementaXYZ();
        System.out.println("\nDespués de incrementaXYZ():");
        System.out.println("x = " + d.getX());
        System.out.println("y = " + d.getY());
        System.out.println("z = " + d.getZ());

        d.incrementaXZ();
        System.out.println("\nDespués de incrementaXZ():");
        System.out.println("x = " + d.getX());
        System.out.println("z = " + d.getZ());

        d.incrementaYZ();
        System.out.println("\nDespués de incrementaYZ():");
        System.out.println("y = " + d.getY());
        System.out.println("z = " + d.getZ());

        d.incrementaZ();
        System.out.println("\nDespués de incrementaZ():");
        System.out.println("z = " + d.getZ());
    }
}
