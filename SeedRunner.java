import java.nio.file.Files;
import java.nio.file.Paths;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class SeedRunner {
    public static void main(String[] args) {
        // Use port 6543 (transaction pooler) or 5432 (session pooler). We will use 6543.
        String url = "jdbc:postgresql://aws-0-ap-northeast-1.pooler.supabase.com:6543/postgres";
        String user = "postgres.pylgfxacjnekbnlyyvyj";
        String pass = "XoLwPqhI9p5slBwS";

        try {
            System.out.println("Reading SQL file...");
            String sql = new String(Files.readAllBytes(Paths.get("retail-india-seed.sql")));
            
            System.out.println("Connecting to Supabase Database...");
            try (Connection conn = DriverManager.getConnection(url, user, pass);
                 Statement stmt = conn.createStatement()) {
                
                System.out.println("Executing seed script...");
                stmt.execute(sql);
                System.out.println("Seed script executed successfully!");
                
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
