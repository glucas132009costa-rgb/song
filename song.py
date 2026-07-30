import subprocess
import time

def criar_musica(nome, artista, album, duracao, genero, ano):
    processo = subprocess.Popen(
        ['python', 'musica.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    respostas = (
        f'{nome}\n'
        f'{artista}\n'
        f'{album}\n'
        f'{duracao}\n'
        f'{genero}\n'
        f'{ano}\n'
    )

    saida, erro = processo.communicate(respostas)

    time.sleep(0.5)

    print(saida)
    if erro:
        print(erro)

musicas = [
    # Section.80 (2011)
    ("Fuck Your Ethnicity", "Kendrick Lamar", "Section.80", "2:39", "Conscious Hip Hop", 2011),
    ("Hol' Up", "Kendrick Lamar", "Section.80", "2:53", "Hip Hop", 2011),
    ("A.D.H.D", "Kendrick Lamar", "Section.80", "3:35", "Hip Hop", 2011),
    ("No Make-Up (Her Vice)", "Kendrick Lamar", "Section.80", "3:52", "Conscious Hip Hop", 2011),
    ("Tammy's Song (Her Evils)", "Kendrick Lamar", "Section.80", "2:45", "Hip Hop", 2011),
    ("Chapter Six", "Kendrick Lamar", "Section.80", "3:41", "Hip Hop", 2011),
    ("Ronald Reagan Era", "Kendrick Lamar", "Section.80", "4:33", "West Coast Hip Hop", 2011),
    ("Poe Mans Dreams (His Vice)", "Kendrick Lamar", "Section.80", "4:14", "Conscious Hip Hop", 2011),
    ("The Spiteful Chant", "Kendrick Lamar", "Section.80", "5:00", "Hip Hop", 2011),
    ("Chapter Ten", "Kendrick Lamar", "Section.80", "1:56", "Hip Hop", 2011),
    ("Keisha's Song (Her Pain)", "Kendrick Lamar", "Section.80", "3:47", "Conscious Hip Hop", 2011),
    ("Rigamortus", "Kendrick Lamar", "Section.80", "2:48", "Jazz Rap", 2011),
    ("Kush & Corinthians", "Kendrick Lamar", "Section.80", "5:02", "Conscious Hip Hop", 2011),
    ("Blow My High (Members Only)", "Kendrick Lamar", "Section.80", "3:37", "Hip Hop", 2011),
    ("Ab-Soul's Outro", "Kendrick Lamar", "Section.80", "5:50", "Hip Hop", 2011),
    ("HiiiPoWeR", "Kendrick Lamar", "Section.80", "4:39", "Conscious Hip Hop", 2011),

    # good kid, m.A.A.d city (2012)
    ("Sherane a.k.a Master Splinter's Daughter", "Kendrick Lamar", "good kid, m.A.A.d city", "4:33", "Hip Hop", 2012),
    ("Bitch, Don't Kill My Vibe", "Kendrick Lamar", "good kid, m.A.A.d city", "5:10", "Hip Hop", 2012),
    ("Backseat Freestyle", "Kendrick Lamar", "good kid, m.A.A.d city", "3:32", "Hip Hop", 2012),
    ("The Art of Peer Pressure", "Kendrick Lamar", "good kid, m.A.A.d city", "5:24", "Conscious Hip Hop", 2012),
    ("Money Trees", "Kendrick Lamar", "good kid, m.A.A.d city", "6:26", "Hip Hop", 2012),
    ("Poetic Justice", "Kendrick Lamar", "good kid, m.A.A.d city", "5:00", "Hip Hop", 2012),
    ("good kid", "Kendrick Lamar", "good kid, m.A.A.d city", "3:34", "Hip Hop", 2012),
    ("m.A.A.d city", "Kendrick Lamar", "good kid, m.A.A.d city", "5:50", "West Coast Hip Hop", 2012),
    ("Swimming Pools (Drank)", "Kendrick Lamar", "good kid, m.A.A.d city", "5:13", "Hip Hop", 2012),
    ("Sing About Me, I'm Dying of Thirst", "Kendrick Lamar", "good kid, m.A.A.d city", "12:03", "Conscious Hip Hop", 2012),
    ("Real", "Kendrick Lamar", "good kid, m.A.A.d city", "7:23", "Hip Hop", 2012),
    ("Compton", "Kendrick Lamar", "good kid, m.A.A.d city", "4:08", "West Coast Hip Hop", 2012),
        # To Pimp a Butterfly (2015)
    ("Wesley's Theory", "Kendrick Lamar", "To Pimp a Butterfly", "4:47", "Jazz Rap", 2015),
    ("For Free? (Interlude)", "Kendrick Lamar", "To Pimp a Butterfly", "2:10", "Jazz Rap", 2015),
    ("King Kunta", "Kendrick Lamar", "To Pimp a Butterfly", "3:54", "Funk Rap", 2015),
    ("Institutionalized", "Kendrick Lamar", "To Pimp a Butterfly", "4:31", "Conscious Hip Hop", 2015),
    ("These Walls", "Kendrick Lamar", "To Pimp a Butterfly", "5:00", "Jazz Rap", 2015),
    ("u", "Kendrick Lamar", "To Pimp a Butterfly", "4:28", "Conscious Hip Hop", 2015),
    ("Alright", "Kendrick Lamar", "To Pimp a Butterfly", "3:39", "Hip Hop", 2015),
    ("For Sale? (Interlude)", "Kendrick Lamar", "To Pimp a Butterfly", "4:51", "Experimental Hip Hop", 2015),
    ("Momma", "Kendrick Lamar", "To Pimp a Butterfly", "4:43", "Jazz Rap", 2015),
    ("Hood Politics", "Kendrick Lamar", "To Pimp a Butterfly", "4:52", "Hip Hop", 2015),
    ("How Much a Dollar Cost", "Kendrick Lamar", "To Pimp a Butterfly", "4:21", "Conscious Hip Hop", 2015),
    ("Complexion (A Zulu Love)", "Kendrick Lamar", "To Pimp a Butterfly", "4:23", "Jazz Rap", 2015),
    ("The Blacker the Berry", "Kendrick Lamar", "To Pimp a Butterfly", "5:28", "Hardcore Hip Hop", 2015),
    ("You Ain't Gotta Lie (Momma Said)", "Kendrick Lamar", "To Pimp a Butterfly", "4:01", "Jazz Rap", 2015),
    ("i", "Kendrick Lamar", "To Pimp a Butterfly", "5:36", "Hip Hop", 2015),
    ("Mortal Man", "Kendrick Lamar", "To Pimp a Butterfly", "12:07", "Conscious Hip Hop", 2015),

    # untitled unmastered. (2016)
    ("untitled 01 | 08.19.2014.", "Kendrick Lamar", "untitled unmastered.", "4:08", "Experimental Hip Hop", 2016),
    ("untitled 02 | 06.23.2014.", "Kendrick Lamar", "untitled unmastered.", "4:18", "Jazz Rap", 2016),
    ("untitled 03 | 05.28.2013.", "Kendrick Lamar", "untitled unmastered.", "2:34", "Hip Hop", 2016),
    ("untitled 04 | 08.14.2014.", "Kendrick Lamar", "untitled unmastered.", "4:24", "Jazz Rap", 2016),
    ("untitled 05 | 09.21.2014.", "Kendrick Lamar", "untitled unmastered.", "5:38", "Jazz Rap", 2016),
    ("untitled 06 | 06.30.2014.", "Kendrick Lamar", "untitled unmastered.", "3:28", "Hip Hop", 2016),
    ("untitled 07 | 2014–2016", "Kendrick Lamar", "untitled unmastered.", "8:16", "Experimental Hip Hop", 2016),
    ("untitled 08 | 09.06.2014.", "Kendrick Lamar", "untitled unmastered.", "3:56", "Jazz Rap", 2016),

    # DAMN. (2017)
    ("BLOOD.", "Kendrick Lamar", "DAMN.", "1:58", "Hip Hop", 2017),
    ("DNA.", "Kendrick Lamar", "DAMN.", "3:05", "Hip Hop", 2017),
    ("YAH.", "Kendrick Lamar", "DAMN.", "2:40", "Hip Hop", 2017),
    ("ELEMENT.", "Kendrick Lamar", "DAMN.", "3:28", "Hip Hop", 2017),
    ("FEEL.", "Kendrick Lamar", "DAMN.", "3:34", "Conscious Hip Hop", 2017),
    ("LOYALTY.", "Kendrick Lamar", "DAMN.", "3:47", "Hip Hop", 2017),
    ("PRIDE.", "Kendrick Lamar", "DAMN.", "4:35", "Hip Hop", 2017),
    ("HUMBLE.", "Kendrick Lamar", "DAMN.", "2:57", "Hip Hop", 2017),
    ("LUST.", "Kendrick Lamar", "DAMN.", "5:07", "Hip Hop", 2017),
    ("LOVE.", "Kendrick Lamar", "DAMN.", "3:33", "Hip Hop", 2017),
    ("XXX.", "Kendrick Lamar", "DAMN.", "4:14", "Hip Hop", 2017),
    ("FEAR.", "Kendrick Lamar", "DAMN.", "7:40", "Conscious Hip Hop", 2017),
    ("GOD.", "Kendrick Lamar", "DAMN.", "4:08", "Hip Hop", 2017),
    ("DUCKWORTH.", "Kendrick Lamar", "DAMN.", "4:08", "Conscious Hip Hop", 2017),
        # Mr. Morale & the Big Steppers (2022)
    ("United in Grief", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "4:15", "Conscious Hip Hop", 2022),
    ("N95", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "3:15", "Hip Hop", 2022),
    ("Worldwide Steppers", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "3:23", "Hip Hop", 2022),
    ("Die Hard", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "4:01", "R&B / Hip Hop", 2022),
    ("Father Time", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "3:43", "Conscious Hip Hop", 2022),
    ("Rich Spirit", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "3:23", "Hip Hop", 2022),
    ("We Cry Together", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "5:41", "Conscious Hip Hop", 2022),
    ("Purple Hearts", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "5:35", "R&B / Hip Hop", 2022),
    ("Count Me Out", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "4:43", "Conscious Hip Hop", 2022),
    ("Crown", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "4:24", "Experimental Hip Hop", 2022),
    ("Silent Hill", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "3:42", "Hip Hop", 2022),
    ("Savior", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "3:50", "Conscious Hip Hop", 2022),
    ("Savior (Interlude)", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "2:32", "Hip Hop", 2022),
    ("Auntie Diaries", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "4:41", "Conscious Hip Hop", 2022),
    ("Mr. Morale", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "3:32", "Hip Hop", 2022),
    ("Mother I Sober", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "6:42", "Conscious Hip Hop", 2022),
    ("Mirror", "Kendrick Lamar", "Mr. Morale & the Big Steppers", "4:16", "Hip Hop", 2022),

    # GNX (2024)
    ("wacced out murals", "Kendrick Lamar", "GNX", "5:17", "West Coast Hip Hop", 2024),
    ("squabble up", "Kendrick Lamar", "GNX", "2:37", "West Coast Hip Hop", 2024),
    ("luther", "Kendrick Lamar", "GNX", "2:57", "R&B / Hip Hop", 2024),
    ("man at the garden", "Kendrick Lamar", "GNX", "3:53", "Hip Hop", 2024),
    ("hey now", "Kendrick Lamar", "GNX", "3:37", "West Coast Hip Hop", 2024),
    ("reincarnated", "Kendrick Lamar", "GNX", "4:35", "Conscious Hip Hop", 2024),
    ("tv off", "Kendrick Lamar", "GNX", "3:40", "West Coast Hip Hop", 2024),
    ("dodger blue", "Kendrick Lamar", "GNX", "2:11", "West Coast Hip Hop", 2024),
    ("peekaboo", "Kendrick Lamar", "GNX", "2:35", "Hip Hop", 2024),
    ("heart pt. 6", "Kendrick Lamar", "GNX", "4:52", "Conscious Hip Hop", 2024),
    ("gnx", "Kendrick Lamar", "GNX", "3:13", "West Coast Hip Hop", 2024),
    ("gloria", "Kendrick Lamar", "GNX", "4:47", "R&B / Hip Hop", 2024),

    # Singles (fora dos álbuns)

    ("The Heart Part 4", "Kendrick Lamar", "The Heart Part 4", "4:53", "Hip Hop", 2017),
    ("The Heart Part 5", "Kendrick Lamar", "The Heart Part 5", "5:32", "Conscious Hip Hop", 2022),

    ("All the Stars", "Kendrick Lamar & SZA", "All the Stars", "3:54", "R&B / Hip Hop", 2018),
    ("King's Dead", "Jay Rock, Kendrick Lamar, Future & James Blake", "King's Dead", "3:45", "Hip Hop", 2018),

    ("Black Panther", "Kendrick Lamar", "Black Panther", "2:10", "Hip Hop", 2018),
    ("Pray For Me", "The Weeknd & Kendrick Lamar", "Pray For Me", "3:31", "Pop / Hip Hop", 2018),

    ("Like That", "Future, Metro Boomin & Kendrick Lamar", "Like That", "4:27", "Hip Hop", 2024),
    ("euphoria", "Kendrick Lamar", "euphoria", "6:23", "Hip Hop", 2024),
    ("6:16 in LA", "Kendrick Lamar", "6:16 in LA", "3:45", "Conscious Hip Hop", 2024),
    ("Meet the Grahams", "Kendrick Lamar", "Meet the Grahams", "6:54", "Conscious Hip Hop", 2024),
    ("Not Like Us", "Kendrick Lamar", "Not Like Us", "4:34", "West Coast Hip Hop", 2024),
    ("Watch the Party Die", "Kendrick Lamar", "Watch the Party Die", "5:06", "Conscious Hip Hop", 2024),
]

for musica, artista, album, duracao, genero,ano in musicas:
    criar_musica(
        musica,
        artista,
        album,
        duracao,
        genero,
        ano
    )