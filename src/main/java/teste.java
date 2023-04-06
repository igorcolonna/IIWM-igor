
public class teste {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int rows = 10;
		int quant = 25;
		//int cols = quant/2;
		int cols = (int) Math.ceil((double)quant/rows);
		System.out.println((double) quant/rows);
		System.out.println(cols);
	}

}
