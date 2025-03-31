public class AlgebraVectorial3D {
    private double x, y, z;

    public AlgebraVectorial3D(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public AlgebraVectorial3D suma(AlgebraVectorial3D b) {
        return new AlgebraVectorial3D(this.x + b.x, this.y + b.y, this.z + b.z);
    }

    public AlgebraVectorial3D multiplicarEscalar(double escalar) {
        return new AlgebraVectorial3D(this.x * escalar, this.y * escalar, this.z * escalar);
    }

    public double norma() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public AlgebraVectorial3D normalizar() {
        double norma = norma();
        return norma != 0 ? new AlgebraVectorial3D(x / norma, y / norma, z / norma) : null;
    }

    public double productoPunto(AlgebraVectorial3D b) {
        return this.x * b.x + this.y * b.y + this.z * b.z;
    }

    public AlgebraVectorial3D productoCruz(AlgebraVectorial3D b) {
        return new AlgebraVectorial3D(
            this.y * b.z - this.z * b.y,
            this.z * b.x - this.x * b.z,
            this.x * b.y - this.y * b.x
        );
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ", " + z + ")";
    }

    public static void main(String[] args) {
        AlgebraVectorial3D a = new AlgebraVectorial3D(1, 2, 3);
        AlgebraVectorial3D b = new AlgebraVectorial3D(4, 5, 6);

        System.out.println("Suma: " + a.suma(b));
        System.out.println("Multiplicación por escalar: " + a.multiplicarEscalar(3));
        System.out.println("Norma de a: " + a.norma());
        System.out.println("Vector normalizado de a: " + a.normalizar());
        System.out.println("Producto punto de a y b: " + a.productoPunto(b));
        System.out.println("Producto cruz de a y b: " + a.productoCruz(b));
    }
}
