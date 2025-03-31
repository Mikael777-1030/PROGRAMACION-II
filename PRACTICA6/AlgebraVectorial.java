public class AlgebraVectorial {

    public static boolean sonPerpendicularesAB(double[] a, double[] b) {
        return norma(vectorSuma(a, b)) == norma(vectorResta(a, b));
    }

    public static boolean sonMutuamentePerpendiculares(double[] a, double[] b) {
        return sonPerpendicularesAB(a, b) && norma(a) == norma(b);
    }

    public static boolean productoPunto(double[] a, double[] b) {
        return productoInterno(a, b) == 0;
    }

    public static double normaCuadrado(double[] a) {
        return Math.pow(norma(a), 2);
    }

    public static boolean sonParalelosEscalar(double[] a, double[] b) {
        if (b[0] == 0 && b[1] == 0) return false;
        double r = a[0] / b[0];
        return (a[1] / b[1]) == r;
    }

    public static boolean sonParalelosProductoCruz(double[] a, double[] b) {
        return (a[0] * b[1] - a[1] * b[0]) == 0;
    }

    public static double[] proyeccionOrtogonal(double[] a, double[] b) {
        double escalar = productoInterno(a, b) / productoInterno(b, b);
        return new double[]{escalar * b[0], escalar * b[1]};
    }

    public static double componenteEnB(double[] a, double[] b) {
        return productoInterno(a, b) / norma(b);
    }

    private static double productoInterno(double[] a, double[] b) {
        return a[0] * b[0] + a[1] * b[1];
    }

    private static double norma(double[] v) {
        return Math.sqrt(v[0] * v[0] + v[1] * v[1]);
    }

    private static double[] vectorSuma(double[] a, double[] b) {
        return new double[]{a[0] + b[0], a[1] + b[1]};
    }

    private static double[] vectorResta(double[] a, double[] b) {
        return new double[]{a[0] - b[0], a[1] - b[1]};
    }

    public static void main(String[] args) {
        double[] a = {3, 4};
        double[] b = {6, 8};

        System.out.println("¿Son perpendiculares? " + sonPerpendicularesAB(a, b));
        System.out.println("Proyección de a sobre b: [" + proyeccionOrtogonal(a, b)[0] + ", " + proyeccionOrtogonal(a, b)[1] + "]");
        System.out.println("Componente de a en dirección de b: " + componenteEnB(a, b));
    }
}
