import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;


public class Percolation {
    private WeightedQuickUnionUF unionFinder;
    private boolean[][] grid;
    private boolean OPEN = true;
    private boolean FULL = false;
    private int numOpen;
    private int upperRow;
    private int lowerRow;
    
    
    public static void main(String[] args)   {
        int n = StdIn.readInt();
        Percolation p = new Percolation(n);
        
        while (!StdIn.isEmpty()) {
            int col = StdIn.readInt();
            int row = StdIn.readInt();
            StdOut.println(p.isFull(1,1));
            
            if (p.isOpen(col, row)) {
                StdOut.println("Already open");
                continue;
            }
            p.open(col, row);
            StdOut.println(col + " " + row);
            
            if (p.percolates()) {
                StdOut.println("percolates!");
                StdOut.println("p = "+ (double)p.numberOfOpenSites()/(n*n));
                break;
            }
        }
    
    }
    
    // create n-by-n grid, with all sites blocked
    public Percolation(int n)     {
        unionFinder = new WeightedQuickUnionUF(n*n+2);
        upperRow = n*n;
        lowerRow = n*n+1;
        grid = new boolean[n][n];
        numOpen = 0;
        for(int i = 0; i < n; i ++) {
            for (int j = 0; j < n; j++) {
                grid [i][j] = FULL;
            }
        }

    }  
   // open site (row, col) if it is not open already 
    public    void open(int row, int col)    {
        row = row-1;
        col = col-1;
        if (grid[row][col]) {
            return;
        }
        grid[row][col] = OPEN;
        connectNeighbours(row, col);
        numOpen++;

    }
        
    private void connectNeighbours(int row, int col) {
        int id = getId(row, col);
        if (row != 0) {
            if (grid[row-1][col]){
                unionFinder.union(id, getId(row-1, col));
            }
        }
        if (row != grid.length - 1) {
            if (grid[row+1][col]){
                unionFinder.union(id, getId(row+1, col));
            }
        }
        if (col != 0) {
            if (grid[row][col-1]){
                unionFinder.union(id, getId(row, col-1));
            }
        }
        if (col != grid.length - 1) {
            if (grid[row][col+1]){
                unionFinder.union(id, getId(row, col+1));
            } 
        }
    }

    private int getId(int row, int col) {
        int id = row*grid.length + col;
        return id;
    }
    
     // is site (row, col) open?
    public boolean isOpen(int row, int col) {
        return grid[row-1][col-1];
    }
     // is site (row, col) full?
    public boolean isFull(int row, int col) {
        return !grid[row-1][col-1];
    }
      // number of open sites
    public     int numberOfOpenSites() {
        return numOpen;
    }
    // does the system percolate?
    public boolean percolates()   {
       for (int j = 0; j < grid.length; j++) {
           if (grid[0][j]) {
               unionFinder.union(upperRow, getId(0, j));
           } 
           if (grid[grid.length-1][j]) {
               unionFinder.union(lowerRow, getId(grid.length-1, j));
           }
        }
        return unionFinder.connected(upperRow, lowerRow);
    }
}


