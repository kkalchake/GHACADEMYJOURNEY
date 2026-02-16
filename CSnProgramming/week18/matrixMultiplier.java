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
    int[][] matrix = new int[ROWS][COLS];
    Random randomNumber = new Random();

    for (int i = 0; i < ROWS; i++) {
      for (int j = 0; j < COLS; j++) {
        matrix[i][j] = randomNumber.nextInt(MAX_RANDOM_VALUE);
      }
    }
    return matrix;
  }

  public static int[][] multiplyMatrices(int[][]matrixA, int[][] matrixB){
    int[][] resultMatrix = new int[ROWS][COLS];

    for (int i = 0; i < ROWS; i++) {
      for (int j = 0; j < COLS; j++) {
        int sum = 0;
        for (int k = 0; k < COLS; k++) {
          sum += matrixA[i][k] * matrixB[k][j];
        }
        resultMatrix[i][j] = sum;
      }
    }
    return resultMatrix;
  }

  public static void printMatrix(int[][] matrix) {
    for (int i = 0; i < ROWS; i++) {
      for (int j = 0; j < COLS; j++) {
        System.out.print(matrix[i][j] + " ");
      }
      System.out.println();
    }
  }
}
