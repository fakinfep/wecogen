import dominate
import rand_gen

def generate_random_website():
    generate_site_indexpage()
    generate_site_aboutpage()
    generate_site_contentpage()
    generate_site_404page()

def generate_site_indexpage():
    doc = dominate.document.title(rand_gen.GenerateRandomTitle())
    with doc.head:
        link(rel='stylesheet', href='style.css')
        link(rel='icon', href='favicon.ico')
    with doc:
        # Random Background Image
        with div(id='background'):
            img(src=rand_gen.GenerateRandomPicture())
        with div(id='header'):
            with div(id='header_content'):
                with div(id='header_title'):
                    h1(rand_gen.GenerateRandomTitle())
                with div(id='header_menu'):
                    with ul():
                        with li():
                            a('Home', href='index.html')
                        with li():
                            a('About', href='about.html')
                        with li():
                            a('Content', href='content.html')
        with div(id='content'):
            with div(id='content_title'):
                h1(rand_gen.GenerateRandomTitle())
            with div(id='content_text'):
                p(rand_gen.GenerateRandomText('wordlist.txt'))
            with div(id='content_image'):
                img(src=rand_gen.GenerateRandomPicture())
        with div(id='footer'):
            p(rand_gen.GenerateRandomText('wordlist.txt'))
    # Add Random Color
    with open('style.css', 'w') as f:
        f.write('body { background-color: ' + rand_gen.GenerateRandomColor() + '; }')
    # Add Random Picture
    with open('favicon.ico', 'wb') as f:
        f.write(rand_gen.GenerateRandomPicture())
    with open('index.html', 'w') as f:
        f.write(doc.render())

def generate_site_aboutpage():
    doc = dominate.document.title(rand_gen.GenerateRandomTitle())
    with doc.head:
        link(rel='stylesheet', href='style.css')
        link(rel='icon', href='favicon.ico')
    with doc:
        with div(id='header'):
            with div(id='header_content'):
                with div(id='header_title'):
                    h1(rand_gen.GenerateRandomTitle())
                with div(id='header_menu'):
                    with ul():
                        with li():
                            a('Home', href='index.html')
                        with li():
                            a('About', href='about.html')
                        with li():
                            a('Content', href='content.html')
        with div(id='content'):
            with div(id='content_title'):
                h1(rand_gen.GenerateRandomTitle())
            with div(id='content_text'):
                p(rand_gen.GenerateRandomText('wordlist.txt'))
            with div(id='content_image'):
                img(src=rand_gen.GenerateRandomPicture())
        with div(id='footer'):
            p(rand_gen.GenerateRandomText('wordlist.txt'))
    with open('about.html', 'w') as f:
        f.write(doc.render())

def generate_site_contentpage():
    doc = dominate.document.title(rand_gen.GenerateRandomTitle())
    with doc.head:
        link(rel='stylesheet', href='style.css')
        link(rel='icon', href='favicon.ico')
    with doc:
        with div(id='header'):
            with div(id='header_content'):
                with div(id='header_title'):
                    h1(rand_gen.GenerateRandomTitle())
                with div(id='header_menu'):
                    with ul():
                        with li():
                            a('Home', href='index.html')
                        with li():
                            a('About', href='about.html')
                        with li():
                            a('Content', href='content.html')
        with div(id='content'):
            with div(id='content_title'):
                h1(rand_gen.GenerateRandomTitle())
            with div(id='content_text'):
                p(rand_gen.GenerateRandomText('wordlist.txt'))
            with div(id='content_image'):
                img(src=rand_gen.GenerateRandomPicture())
        with div(id='footer'):
            p(rand_gen.GenerateRandomText('wordlist.txt'))
    with open('content.html', 'w') as f:
        f.write(doc.render())

def generate_site_404page():
    doc = dominate.document.title(rand_gen.GenerateRandomTitle())
    with doc.head:
        link(rel='stylesheet', href='style.css')
        link(rel='icon', href='favicon.ico')
    with doc:
        with div(id='header'):
            with div(id='header_content'):
                with div(id='header_title'):
                    h1(rand_gen.GenerateRandomTitle())
                with div(id='header_menu'):
                    with ul():
                        with li():
                            a('Home', href='index.html')
                        with li():
                            a('About', href='about.html')
                        with li():
                            a('Content', href='content.html')
        with div(id='content'):
            with div(id='content_title'):
                h1(rand_gen.GenerateRandomTitle())
            with div(id='content_text'):
                p(rand_gen.GenerateRandomText('wordlist.txt'))
            with div(id='content_image'):
                img(src=rand_gen.GenerateRandomPicture())
        with div(id='footer'):
            p(rand_gen.GenerateRandomText('wordlist.txt'))
    with open('404.html', 'w') as f:
        f.write(doc.render())