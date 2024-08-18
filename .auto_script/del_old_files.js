const fs = require('fs');
const path = require('path');

const fileName = '中文git_linux';
const filePath = path.resolve(fileName);

fs.access(filePath, fs.constants.F_OK, (err) => {
  if (!err) {
    console.log(`找到旧文件【${fileName}】，正在删除...`);
    fs.unlink(filePath, (err) => {
      if (err) throw err;
      console.log(`文件【${fileName}】已删除`);
    });
  } else {
    console.log(`未找到旧文件【${fileName}】`);
  }
});
