import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;


public class PercolationStats {
    private double m;
    private double s;
    private double lo;
    private double hi;
       // perform trials independent experiments on an n-by-n grid
    public PercolationStats(int n, int trials) {
        if (n < 1 || trials < 1) {
            throw new IllegalArgumentException();
        }
        
        int gridSize = n*n;
        int upperRange = n+1;
        double[] pThreshold = new double[trials];
        
        for (int i = 0; i < trials; i++) { 
            Percolation p = new Percolation(n);
            
            while (!p.percolates()) {
                int col = StdRandom.uniform(1, upperRange);
                int row = StdRandom.uniform(1, upperRange);
                if (p.isOpen(col, row)) {
                    continue;
                }
                p.open(col, row);
            }
            pThreshold[i] = (double) p.numberOfOpenSites()/(gridSize);
        }
        m = StdStats.mean(pThreshold);   
        s = StdStats.stddev(pThreshold);
        lo = m - 1.96*s / Math.sqrt(trials);
        hi = m + 1.96*s / Math.sqrt(trials);
    }

    public double mean() {
        return m;
    }
    public double stddev()     {
        return s;
    }
       // sample standard deviation of percolation threshold
    public double confidenceLo() {
        return lo;
    }                 // low  endpoint of 95% confidence interval
    public double confidenceHi()  {
        return hi;
    }                // high endpoint of 95% confidence interval

    public static void main(String[] args) {
        int gridSize = Integer.parseInt(args[0]);
        int numTrials = Integer.parseInt(args[1]);
        PercolationStats experiment = new PercolationStats(gridSize, numTrials);
        System.out.println("mean\t\t\t= " + experiment.mean());
        System.out.println("stddev\t\t\t= " + experiment.stddev());
        System.out.println("95% confidence interval\t= [" + experiment.confidenceHi() + ", " + experiment.confidenceLo() + "]");
    }
}