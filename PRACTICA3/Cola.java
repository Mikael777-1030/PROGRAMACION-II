class Cola {
	
	private long[] arreglo;
	private int inicio;
	private int fin;
	private int nroElementos;
	private int n;
	
	
	public Cola(int n) {
		this.n = n;
		arreglo = new long[n];
		inicio = 0;
		fin = -1;
		nroElementos = 0;
	}
	public void insert(long e) { 
		if (!isFull()) {
			if (fin == this.n - 1) 
				fin = -1;
			fin++;            
			arreglo[fin] = e; 
			nroElementos++;   
		} else 
			System.out.println("Cola llena.");
	}
	public long remove() {
		long e = Long.MIN_VALUE;
		if (!isEmpty()) {
			e = arreglo[inicio]; 
			inicio++;                
			if (inicio == this.n)    
				inicio = 0;
			nroElementos--;          
		} else
			System.out.println("Cola vac�a.");
		return e;
	}
	public long peek() { 
		long e = Long.MIN_VALUE;
		if (!isEmpty())
			e = arreglo[inicio]; 
		else
			System.out.println("Cola vac�a.");
		return e;
	}
	public boolean isEmpty() { 
		return (nroElementos == 0);
	}
	public boolean isFull() { 
		return (nroElementos == this.n);
	}
	public int size() {
		return nroElementos;
	}
}
