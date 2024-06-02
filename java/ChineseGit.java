import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

/*
    For DEV:
        此代码有众多(11)错误，建议从头重写。
*/

public class ChineseGitUpdater {
    private static final String SCRIPT_PATH = System.getProperty("user.dir");

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入版本号：");
        String version = scanner.nextLine();

        String newFilename = downloadUpdateFile(version);
        if (newFilename != null) {
            replaceCurrentProgram(newFilename);
        }
    }

    public static String downloadUpdateFile(String version) {
        // 根据版本确定下载 URL
        String downloadUrl = "https://github.com/DuckDuckStudio/Chinese_git/releases/download/" + version + "/Pack_Version_Update.exe";
        try {
            // 发送GET请求
            URL url = new URL(downloadUrl);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");

            // 获取响应码
            int responseCode = connection.getResponseCode();

            if (responseCode == HttpURLConnection.HTTP_OK) {
                // 读取响应流并保存为文件
                String newFilename = SCRIPT_PATH + "\\中文git更新程序.exe";
                FileOutputStream outputStream = new FileOutputStream(newFilename);

                byte[] buffer = new byte[1024];
                int bytesRead;
                while ((bytesRead = connection.getInputStream().read(buffer)) != -1) {
                    outputStream.write(buffer, 0, bytesRead);
                }
                outputStream.close();
                System.out.println("[✓] 更新成功下载。");
                return newFilename;
            } else {
                System.out.println("[✕] 下载更新文件时出错: " + responseCode);
                return null;
            }
        } catch (IOException e) {
            System.out.println("[✕] 下载更新文件时出错: " + e.getMessage());
            return null;
        }
    }

    public static void replaceCurrentProgram(String newFilename) {
        try {
            // 使用Files.move方法替换当前程序
            Path newFilePath = Paths.get(newFilename);
            Path currentFilePath = Paths.get(SCRIPT_PATH, "中文git更新程序.exe");
            Files.move(newFilePath, currentFilePath, StandardCopyOption.REPLACE_EXISTING);
            System.out.println("[✓] 更新程序已成功更新。");
        } catch (IOException e) {
            System.out.println("[✕] 替换当前更新程序时出错: " + e.getMessage());
        }
    }
}
