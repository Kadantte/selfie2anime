import json
from string import Template


def me(event, context):
    uuid = event['queryStringParameters']['uuid']

    image_url_escaped = 'https://selfie2anime.com/outgoing/{}.jpg'.format(uuid)
    viewer_url_escaped = 'https://api.selfie2anime.com/analysis/me?uuid={}'.format(uuid)

    content = Template('''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">

        <meta property="og:url" content="$viewer_url_escaped" />
        <meta property="og:type" content="website" />
        <meta property="og:title" content="Selfie2Anime | It's Me!" />
        <meta property="og:description" content="What do YOU look like in Anime?" />
        <meta property="og:image" content="$image_url_escaped" />

        <link rel="image_src" type="image/jpg" href="$image_url_escaped" />

        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        <script>
            (adsbygoogle = window.adsbygoogle || []).push({
                google_ad_client: "ca-pub-9169830803956537",
                enable_page_level_ads: true,
            });
        </script>

        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-71336829-28"></script>
        <script>
            window.dataLayer = window.dataLayer || [];

            function gtag() {
                dataLayer.push(arguments);
            }

            gtag("js", new Date());
            gtag("config", "UA-71336829-28");
        </script>

        <link rel="icon" href="https://selfie2anime.com/favicon.ico">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Merriweather+Sans:400,400i,700,700i">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css">

        <title>Selfie2Anime | It's Me!</title>
        <style>
            * {
                -ms-text-size-adjust: 100%;
                -webkit-text-size-adjust: 100%;
            }

            html,
            body {
                margin: 0 auto !important;
                padding: 0 !important;
                height: 100% !important;
                width: 100% !important;
                background: #f1f1f1;
            }

            div[style*="margin: 16px 0"] {
                margin: 0 !important;
            }

            table,
            td {
                mso-table-lspace: 0 !important;
                mso-table-rspace: 0 !important;
            }

            table {
                border-spacing: 0 !important;
                border-collapse: collapse !important;
                table-layout: fixed !important;
                margin: 0 auto !important;
            }

            img {
                -ms-interpolation-mode: bicubic;
            }

            a {
                text-decoration: none;
            }

            .bg_primary {
                background: #f06292;
            }

            .text_primary {
                color: #f06292;
                font-weight: bold;
            }

            .bg_white {
                background: #fff;
            }

            .bg_dark {
                background: rgba(0, 0, 0, .8);
            }

            .email-section {
                padding: 2.5em;
            }

            h1,
            h2 {
                font-family: 'Merriweather Sans', sans-serif;
                color: #000;
                margin-top: 0;
            }

            body {
                font-family: 'Merriweather Sans', sans-serif;
                font-weight: 400;
                font-size: 18px;
                line-height: 1.8;
                color: rgba(0, 0, 0, .7);
            }

            a {
                color: #f06292;
                font-weight: bold;
            }

            .logo h1 {
                margin: 0;
            }

            .logo h1 a {
                color: #000;
                font-size: 24px;
                font-weight: 700;
                text-transform: uppercase;
                font-family: 'Merriweather Sans', sans-serif;
            }

            .navigation li {
                list-style: none;
                display: inline-block;
                margin-left: 5px;
                font-size: 12px;
                font-weight: 700;
                text-transform: uppercase;
            }

            .navigation li a {
                color: rgba(0, 0, 0, .6);
            }

            .heading-section h2 {
                color: #000;
                font-size: 28px;
                margin-top: 0;
                line-height: 1.4;
                font-weight: 700;
            }

            .heading-section .subheading {
                margin-bottom: 20px !important;
                display: inline-block;
                font-size: 13px;
                text-transform: uppercase;
                letter-spacing: 2px;
                color: rgba(0, 0, 0, .4);
                position: relative;
            }

            .heading-section .subheading::after {
                position: absolute;
                left: 0;
                right: 0;
                bottom: -10px;
                content: '';
                width: 100%;
                height: 2px;
                background: #f5564e;
                margin: 0 auto;
            }

            .heading-section-white {
                color: rgba(255, 255, 255, .8);
            }

            .heading-section-white h2 {
                line-height: 1em;
                padding-bottom: 0;
            }

            .heading-section-white h2 {
                color: #fff;
            }

            .heading-section-white .subheading {
                margin-bottom: 0;
                display: inline-block;
                font-size: 13px;
                text-transform: uppercase;
                letter-spacing: 2px;
                color: rgba(255, 255, 255, .4);
            }

            .spinner-container {
                position: absolute;
                display: flex;
                flex-direction: row;
                flex-wrap: wrap;
                width: 100%;
                height: 100%;
                justify-content: center;
                align-items: center;
                background-color: rgba(240, 98, 146, 0.5);
            }

            .spinner {
                border: 10px solid #fff;
                border-top: 10px solid transparent;
                border-radius: 50%;
                width: 50px;
                height: 50px;
                animation: spinner 2s both infinite;
            }

            @keyframes spinner {
                0% {
                    transform: rotate(0deg);
                }

                100% {
                    transform: rotate(360deg);
                }
            }
        </style>
    </head>

    <body width="100%" style="margin: 0; padding: 0 !important; mso-line-height-rule: exactly; background-color: #222;">
        <center style="width: 100%; background-color: #f1f1f1;">
            <div style="max-width: 600px; margin: 0 auto;" class="email-container">
                <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%"
                    style="margin: auto;">
                    <tr>
                        <td valign="top" class="bg_white" style="padding: 1em 2.5em;">
                            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                                <tr>
                                    <td width="60%" class="logo" style="text-align: left;">
                                        <h1>
                                            <a href="https://selfie2anime.com">
                                                Selfie<span class="text_primary">2</span>Anime&nbsp;<span
                                                    class="text_primary">アニメ</span>
                                            </a>
                                        </h1>
                                    </td>
                                    <td width="40%" class="logo" style="text-align: right;">
                                        <a href="https://www.facebook.com/sharer/sharer.php?u=$viewer_url_escaped">
                                            <img width="32" height="32" src="https://selfie2anime.com/email/facebook.png"
                                                alt="Share on Facebook">
                                        </a>
                                        <a href="https://twitter.com/intent/tweet?url=$viewer_url_escaped&text=Hey, this is me as an anime character!&hashtags=selfie2anime"
                                            target="_blank">
                                            <img width="32" height="32" src="https://selfie2anime.com/email/twitter.png"
                                                alt="Share on Twitter">
                                        </a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" class="bg_primary" style="line-height: 0; position: relative;">
                            <div id="spinner-container" class="spinner-container">
                                <div id="spinner" class="spinner"></div>
                                <div id="error"
                                    style="display: none; color: white; font-size: 20pt; line-height: 1.5em; text-align: center;">
                                    <b>Oh No! There was an error!<br> Please try again.</b>
                                </div>
                            </div>
                            <a href="https://selfie2anime.com/" title="Create your own selfie!">
                                <img id="selfie" width="600" height="600" src="https://selfie2anime.com/email/frame.jpg" alt="Your Anime Selfie!"
                                    style="max-width: 100%; height: auto">
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td class="bg_white email-section">
                            <div class="heading-section" style="text-align: center; padding: 0 30px;">
                                <h2>Enjoying Your Selfie?</h2>
                                <p><b>Share it</b> on social media and <a href="https://selfie2anime.com/">create your
                                        own!</a></p>
                            </div>
                            <table width="50%">
                                <tr>
                                    <td>
                                        <div class="text" style="text-align: center">
                                            <a href="https://www.facebook.com/sharer/sharer.php?u=$viewer_url_escaped">
                                                <img width="64" height="64"
                                                    src="https://selfie2anime.com/email/facebook.png"
                                                    alt="Share on Facebook">
                                            </a>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="text" style="text-align: center">
                                            <a href="https://twitter.com/intent/tweet?url=$viewer_url_escaped&text=Hey, this is me as an anime character!&hashtags=selfie2anime"
                                                target="_blank">
                                                <img width="64" height="64" src="https://selfie2anime.com/email/twitter.png"
                                                    alt="Share on Twitter">
                                            </a>
                                        </div>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" class="bg_primary"
                            style="background-image: url(https://selfie2anime.com/email/wall.jpg); background-size: cover; height: 480px;">
                        </td>
                    </tr>
                    <tr>
                        <td class="bg_dark email-section" style="text-align:center;">
                            <div class="heading-section heading-section-white">
                                <p>
                                    Copyright &copy; 2019-2020 by
                                    <a href="https://selfie2anime.com">Selfie2Anime.com</a>
                                </p>
                            </div>
                        </td>
                    </tr>
                </table>
            </div>
        </center>
        <script>
            const FRAME_URL = "https://selfie2anime.com/email/frame.jpg";
            const SELFIE_URL = "$image_url_escaped";

            function fetchImage(url) {
                return new Promise((resolve, reject) => {
                    const image = new Image();
                    image.crossOrigin = "anonymous";
                    image.onerror = () => reject(new Error("Failed to load frame/selfie"));
                    image.onload = () => resolve(image);
                    image.src = url;
                });
            }

            function generateFrame() {
                const canvas = window.document.createElement("canvas");
                const frameImage = fetchImage(FRAME_URL);
                const selfieImage = fetchImage(SELFIE_URL);

                const context = canvas.getContext("2d");
                Promise.all([frameImage, selfieImage])
                    .then(images => {
                        canvas.width = 600;
                        canvas.height = 600;

                        context.drawImage(images[0], 0, 0, 600, 600);
                        context.drawImage(images[1], 93, 113, 407, 407);

                        document.getElementById("selfie").src = canvas.toDataURL("image/jpeg", 1.0);
                        document.getElementById("spinner-container").style.display = "none";
                    })
                    .catch(() => {
                        document.getElementById("spinner").style.display = "none";
                        document.getElementById("error").style.display = "inline";
                    });
            }

            window.addEventListener("load", function () {
                generateFrame();
            });
        </script>
    </body>

    </html>
    ''')
    html_body = content.substitute(image_url_escaped=image_url_escaped, viewer_url_escaped=viewer_url_escaped)

    response = {
        "statusCode": 200,
        "body": html_body,
        "headers": {
            'Content-Type': 'text/html',
        }
    }

    return response
