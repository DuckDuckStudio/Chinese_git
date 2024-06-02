import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

/*
    For DEV:
        忽略此警告:
            The constructor URL(String) is deprecated since version 20
        仍使用 URL() 而非 URI()
        使用过时的构造函数可能是安全的，因为我们只是简单地传递一个URL字符串。
*/

public class ChineseGitUpdater {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("输入要更新到的版本号: ");
            String version = scanner.nextLine();

            String newFilename = null;
            try {
                newFilename = downloadUpdateFile(version);
            } catch (IOException e) {
                System.out.println("发生IO异常: " + e.getMessage());
            }

            if (newFilename != null) {
                replaceCurrentProgram(newFilename);
            }

            System.out.println("按Enter键退出...");
            scanner.nextLine();
        }
    }

    private static String downloadUpdateFile(String version) throws IOException {
        // 下载URL和备用下载URL
        String downloadUrl = "https://github.com/DuckDuckStudio/Chinese_git/releases/download/" + version + "/Chinese_git.exe";
        // String spareDownloadUrl = "https://duckduckstudio.github.io/yazicbs.github.io/Tools/chinese_git/Spare-Download/Chinese_git.exe";
        String newFilename = "中文git.exe";

        URL url = new URL(downloadUrl);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");

        int responseCode = connection.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) {
            try (InputStream inputStream = connection.getInputStream();
                 FileOutputStream outputStream = new FileOutputStream(newFilename)) {
                byte[] buffer = new byte[1024];
                int bytesRead;
                while ((bytesRead = inputStream.read(buffer)) != -1) {
                    outputStream.write(buffer, 0, bytesRead);
                }
            }
            System.out.println("✓ 更新成功下载。");
            return newFilename;
        } else {
            System.out.println("✕ 下载更新文件时出错: HTTP错误码 " + responseCode);
            throw new IOException("下载更新文件时出错: HTTP错误码 " + responseCode);
        }
    }

    private static void replaceCurrentProgram(String newFilename) {
        try {
            Path currentProgramPath = Paths.get(System.getProperty("user.dir"), "中文git.exe");
            Files.move(Paths.get(newFilename), currentProgramPath);
            System.out.println("✓ 程序已成功更新。");
        } catch (IOException e) {
            System.out.println("✕ 替换当前程序时出错: " + e.getMessage());
        }
    }
}
