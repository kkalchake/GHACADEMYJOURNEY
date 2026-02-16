import java.util.Random;

class MatrixMultiplier
{

  static final int MAX_RANDOM_VALUE = 10;

  public static void main (String[] args) throws java.lang.Exception
  {
    int[][] matrixA = makeTwoDMatrixWithRandomValues(4, 5);
    int[][] matrixB = makeTwoDMatrixWithRandomValues(5, 8);

    System.out.println("Matrix A: ");
    printMatrix(matrixA);

    System.out.println("Matrix B: ");
    printMatrix(matrixB);

    int[][] multipliedMatrix = multiplyMatrices(matrixA, matrixB);

    System.out.println("\nResult Matrix: ");
    printMatrix(multipliedMatrix);

  }

  public static int[][] makeTwoDMatrixWithRandomValues(int rows, int cols) {
    int[][] matrix = new int[rows][cols];
    Random randomNumber = new Random();

    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        matrix[i][j] = randomNumber.nextInt(MAX_RANDOM_VALUE);
      }
    }
    return matrix;
  }

  public static int[][] multiplyMatrices(int[][]matrixA, int[][] matrixB){
    int[][] resultMatrix = new int[matrixA.length][matrixB[0].length];
    if (matrixA[0].length != matrixB.length) {
      throw new IllegalArgumentException("Number of columns in matrix A must be equal to number of rows in matrix B");
    }
    for (int i = 0; i < matrixA.length; i++) {
      for (int j = 0; j < matrixB[0].length; j++) {
        int sum = 0;
        for (int k = 0; k < matrixA[0].length; k++) {
          sum += matrixA[i][k] * matrixB[k][j];
        }
        resultMatrix[i][j] = sum;
      }
    }
    return resultMatrix;
  }

  public static void printMatrix(int[][] matrix) {
      for (int[] matrix1 : matrix) {
          for (int j = 0; j < matrix1.length; j++) {
              System.out.print(matrix1[j] + " ");
          }
          System.out.println();
      }
  }
}
