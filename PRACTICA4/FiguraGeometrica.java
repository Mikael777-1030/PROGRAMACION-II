package tarea;
class FiguraGeometrica {
        double area(double radio) {
        return Math.PI * radio * radio;
    }

    public double area(double base, double altura) {
        return base * altura;
    }
    
    
    public double area(double base, double altura, String tipo) {
        if ("triangulo".equalsIgnoreCase(tipo)) {
            return (base * altura) / 2;
        }
        return 0;
    }

    
    double area(double baseMayor, double baseMenor, double altura) {
        return (baseMayor + baseMenor) * altura / 2;
    }
    
    
    public double area(double lado, String tipo) {
        if ("pentagono".equalsIgnoreCase(tipo)) {
            double apotema = lado / (2 * Math.tan(Math.PI / 5));
            double perimetro = 5 * lado;
            return (perimetro * apotema) / 2;
        }
        return 0;
    }

    
    double area(double lado, double apotema) {
        return 5 * lado * apotema / 2;
    }
    
    
    
    double area(double lado, String figura) {
    	double apotema;
      	apotema = lado/(2 * Math.tan(Math.toRadians(36)));
   		apotema = lado/(2 * Math.sqrt(5 - 2 * Math.sqrt(5)));
    	System.out.println(apotema);
        if (figura.equals("pentagono")) {
        	return (5.0/4.0) * lado * lado / Math.sqrt(5 - 2 * Math.sqrt(5));
        	return (1.0/4.0) * lado * lado * Math.sqrt(5 * (5 + 2 * Math.sqrt(5)));
        	return 5 * lado * apotema / 2;
        }
        return 0;
    }
    

    public static void main(String[] args) {
        FiguraGeometrica figura = new FiguraGeometrica();
        System.out.println("Área del círculo: " + figura.area(5));
        System.out.println("Área del rectángulo: " + figura.area(4, 6));
        System.out.println("Área del triángulo: " + figura.area(4, 6, "triangulo"));
        System.out.println("Área del trapecio: " + figura.area(6, 4, 5));
        System.out.println("Área del pentágono: " + figura.area(3, "pentagono"));
    }
}
