import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import java.util.Arrays;

public class UnionFinder {
    
    public static void main(String[] args) {
        int n = StdIn.readInt();
        WeightedQuickUnionUF uf = new WeightedQuickUnionUF(n);
        while (!StdIn.isEmpty()) {
            int p = StdIn.readInt();
            int q = StdIn.readInt();
            if (p >= n || q >= n) {
                continue;
            }
            if (uf.connected(p, q)) {
                StdOut.println("Already connected");
                continue;
            }
            uf.union(p, q);
            StdOut.println(p + " " + q);
        }
        StdOut.println(uf.count() + " components");
    }
}


class WeightedQuickUnionUF {
    int count;
    int[] ids;
    int[] size;
    
    public WeightedQuickUnionUF(int N) {
        count = N;
        ids = new int[N];
        size = new int[N];
        for (int i = 0; i < N; i++) {
            ids[i] = i;
            size[i] = 1;
        }
    }
    
    private int root(int a) {
        while(a != ids[a]) {
            ids[a] = root(ids[a]);
            a = ids[a];
        }
        return a;
    }

    public boolean connected (int a, int b) {
        return root(a) == root(b);
    }
    
    public void union (int a, int b) {
        int rootA = root(a);
        int rootB = root(b);
        
        if (size[rootA] < size[rootB]){
            ids[rootA] = rootB;
            size[rootB] += size[rootA];
        } else {
            ids[rootB] = rootA;
            size[rootA] += size[rootB];
        }
        System.out.println(Arrays.toString(ids));
        System.out.println(Arrays.toString(size));
        count --;
    }
    
    public int count() {
        return count;
    }
}

class QuickUnionUF {
    int count;
    int[] ids;
    
    public QuickUnionUF(int N) {
        count = N;
        ids = new int[N];
        for (int i = 0; i < N; i++) {
            ids[i] = i;
        }
    }
    
    private int root(int a) {
        while(a != ids[a]) {
            a = ids[a];
        }
        return a;
    }

    public boolean connected (int a, int b) {
        return root(a) == root(b);
    }
    
    public void union (int a, int b) {
        int i = root(a);
        int j = root(b);
        ids[i] = j;
        count --;
    }
    
    public int count() {
        return count;
    }
}

class QuickFindUF {
    private int[] connections;
    private int count;
    
    public QuickFindUF(int N) {
        connections = new int[N];
        for (int i=0; i<N;  i++) {
            connections[i] = i;
        }
        count = N;
    }
    
    public boolean connected(int a, int b) {
        return connections[a] == connections[b];
    }
    
    public void union(int a, int b) {
        int aid = connections[a];
        int bid = connections[b];
        for (int i = 0; i < connections.length; i++) {
            if (connections[i] == aid) {
                connections[i] = bid;
            }
        }
        count--;
    }
    
    public int count() {
        return count;
    }
    
    public int[] getConnections() {
        return connections;
    }
}