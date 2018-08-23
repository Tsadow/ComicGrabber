<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Comics</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
    <script src="main.js"></script>
</head>
<body>
    <?php
        // for handling alt text
        $postfixRegex = "(\.png)";

        // get the image file contents of the img/ directory
        $images = glob("img/*.png");

        // iterate through each image and add to <img> element
        foreach($images as $img){
            $altText = "";

            // special case to get alt text for xkcd
            if(strcmp($img, "img/xkcd.com.png") == 0){
                $altFilePath = preg_replace($postfixRegex, '', $img);
                $altFilePath = $altFilePath . ".txt";
                $altFile = fopen($altFilePath, "r") or die("FileNotFoundException: no alt text");
                $altText = fgets($altFile);
                fclose($altFile);
            }

            echo "<img src=" . $img . " title=" . $altText . " >";
        }
    ?>

</body>
</html>