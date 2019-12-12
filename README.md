# slide_html_wrapper  


[https://html.naysok.org/slide_html_wrapper/](https://html.naysok.org/slide_html_wrapper/)  


### slide + web browser  

スライド中で関連資料とかのリンクを開きたい時がある。   

プレゼンテーション再生中に、手早く開くのは不可能。  
MacOS 環境であれば、pdf 化して、Preview.app で全画面表示。ブラウザに、command + tab で随時切り替える
ならば、できるといえばできるが、いちいち面倒。  

とりあえず、全て html にして、すべてブラウザでやっていくのがよいのでは、そのためにスライドのデータから、静的ページにビルドしたい。  


### programmable ??

話が脇道に逸れるが、スタイル、コンテンツ共に、プログラマバブルなドキュメント環境は、html + css くらい？  

html を直で書きたくないので、データとテンプレートからビルドして、静的ページを生成するのが今のところはベター。  


### pdf on html  

スライド制作環境はいくつかあるが、それらのネイティブ形式のファイルを使うのは無理なので、一律で pdf にする。  

pdf を html で表示する方法はあるっぽい。  
```html
<embed>
<object>
<iframe>
```

が、あまり美しくないので却下。  
```html
<img>
```
で扱えれば、普通に html のスクラッチでどうにでもなるので、png や jpg のような画像にしたい。  


### images from pdf  

スライド資料から、連番画像を用意する。  

powerpint, keynote ならば、連番画像の書き出しがあるので問題無し。  

google slide だけ不明。  

- powerpoint, keynote, google slide >> (*.pdf) >> pdf2image via Python  
  // google slide の場合はこれが良さそう。  

- google slide >> (*.pptx) >> powerpoint, keynote  
  // デザイン崩れる  

後者の方が簡単だけど、フォント問題等々あるので、 pdf2image で。  

*src/pdf_to_image.py*


### build html  

静的ページをビルドする。  

ページ数（ファイル数）を取得し、html の文字列を生成する。  

上で生成した文字列と、テンプレートをくっつけて完成。  

*src/build_html.py*


---  