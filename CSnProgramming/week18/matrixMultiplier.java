import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.Random;

class MatrixMultiplier
{
	static final int ROWS = 3;
	static final int COLS = 3;
	static final int MAX_RANDOM_VALUE = 10;
	
	public static void main (String[] args) throws java.lang.Exception
	{
		int[][] matrixA = makeTwoDMatrixWithRandomValues();
		int[][] matrixB = makeTwoDMatrixWithRandomValues();
		
		System.out.println("Matrix A: ");
		printMatrix(matrixA);
		
		System.out.println("Matrix B: ");
		printMatrix(matrixB);
		
		int[][] multipliedMatrix = multiplyMatrices(matrixA, matrixB);
		
		System.out.println("\nResult Matrix: ");
		printMatrix(multipliedMatrix);
		
	}
	
	public static int[][] makeTwoDMatrixWithRandomValues() {
		
	}
	
	public static int[][] muliplyMatrices(){
		
	}
	
	public static void printMatrix(int[][] matrix) {
		
	}
}