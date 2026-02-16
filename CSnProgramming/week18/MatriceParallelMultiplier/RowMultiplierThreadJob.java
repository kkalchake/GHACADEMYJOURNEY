public class RowMultiplierThreadJob implements Runnable {

    private final int[][] matrixA;
    private final int[][] matrixB;
    private final int[][] resultMatrix;
    private final int rowIndex;

    public RowMultiplierThreadJob(int[][] matrixA, int[][] matrixB, int[][] resultMatrix, int rowIndex) {
        this.matrixA = matrixA;
        this.matrixB = matrixB;
        this.resultMatrix = resultMatrix;
        this.rowIndex = rowIndex;
    }

    @Override
    public void run() {
        for (int j = 0; j < matrixB[0].length; j++) {
            int sum = 0;
            for (int k = 0; k < matrixA[0].length; k++) {
                sum += matrixA[rowIndex][k] * matrixB[k][j];
            }
            resultMatrix[rowIndex][j] = sum;
        }
    }
}