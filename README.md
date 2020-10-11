# positivipy
Delivering Positivity with Python
<!-- wp:paragraph -->
<p>I have been posting a daily positive thought to my own Facebook page, "<a rel="noreferrer noopener" href="https://www.facebook.com/positivedailythought" target="_blank">Positive Thoughts Daily</a>", for several years as part of project I started on a whim. I share anything by famous thinkers and creators I read. It was partially inspired by the discipline of "<a href="https://en.wikipedia.org/wiki/Positive_psychology" target="_blank" rel="noreferrer noopener">Positive Psychology</a>".</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Recently I have begun to think about using this dataset of quote images to generate new positive and inspirational quotes. This post details a simple implementation and alternatives I considered to accomplish this goal.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Project Overview</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><li>Export all Facebook post images from my page</li><li>Convert images to quote text with <strong>Optical character recognition</strong> (OCR)</li><li>Data cleaning (via pandas and manual correction)</li><li>Train on past quotes and generate new quotes with Markov Chains</li></ol>

<p>You can read the blog post corresponding to this repo on my blog, Python Marketer: "<a href="https://pythonmarketer.com/2020/10/11/generating-positive-thoughts-with-google-vision-ocr-and-markov-chains/" target="_blank" rel="noreferrer noopener">Generating Positive Thoughts with Google Vision OCR and Markov Chains</a>"
<!-- /wp:list -->
