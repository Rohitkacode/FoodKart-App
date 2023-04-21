# Generated by Django 3.2 on 2023-04-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20230420_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBQVFRgVFhYZGBgVFRYaGBgVHRwWGBkdGBgcHRgcGRocIS4lIx4sIRkcKDgmKy8xNTU1HCQ7QDs0Py40NjEBDAwMEA8QHhISHz8sJCs0NDg2NjE0NDQ2PTY6NTQ0NDQ2MTQ0PTY0NDQ0NDQ0NDQ0NDQ0NDQ0MTQ0NDQ0NDQ0NP/AABEIAOEA4QMBIgACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAABAYCAwUBB//EAD0QAAIBAwMCBAQCBwcEAwAAAAECAAMEERIhMQVRBiJBYRMycYEUoQdSkcHR4fAVYnKCsbPxI0JTsjM0Nf/EABgBAQEBAQEAAAAAAAAAAAAAAAABAwIE/8QAJREBAQACAQQCAQUBAAAAAAAAAAECESEDEjFBUYFhIjJxofAT/9oADAMBAAIRAxEAPwD7NERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBETHI78wMoiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiIHkRObe9RCnSu5P7oWS26iTcXIGw5P5e5ld6pUZm39M4/jJdIktk8yBfvlz7bTPu29GXTmES+n9VK+V8kZ5zkjPtLDTqBhkEEe28peZMsLxqbahup+Yfv+s6mTLLHa2RNVGsGAZTkGbZ0zIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICYOwG5mFxXVFLMcAf1tK9eXrsPiZK7EqASMA7J9zuT9BAndV6joUgbEjyj1+uOw/hOFYsS+T+qf3TFlLIhG5BYHvzmSul251MxGy7Y98/ynN8NML+qJ6NpUs3b/j9s4zNkknknJ+8ndWrbhP8AMfr6f17zmapxppnlutkwDkH2nmqeEyyOLXT6bf6G/un8v5SxpcqSBnBPAPr9O8pKtOhZ3WRoY4/Ub9U+n2/jEukslW6JxOl37lgjnO5GT8wI9D3/AJ+xnbmjMiIgIiICIiAiIgIiICIiAiIgJrqVAoySAO5OBNkgdUp6l4zgg49xAN1Jc6UBc+2AB9SZ7XvtC5K98AHJP5SM7hB33wB39z+ZkKs7OVB5Yrn23yfy2lHO6lds5BY876R6D+Mj3FwXOTsMAADgAcCeXR87Z7/8TVIrodKcZIPG/wCe39fSdakVQHcbksfvx9tvynFsk2J9M79z2A9/m+mJMrkvtj644A9AJzlZJy6wuqgVHLvn1Y/8flNr2r5wNwfX+M6NsgcBWGCowDjcTetPTgcjGDML1L6aa+XDr2rJ9O81afeWT4HfdT3lb6r1X4d9QtFpIVqqhLknUNTOuAB/g5PeXHqW8aTLGPAcTIGYdYu7eg7K1ZNSjLIT51yARsOdiPecWr4pt1TWrMx1adAGG45w2PL7zWcxx4Wm2rEtqGdYx/mxx9/69TLbTcMAR6gH9s+d9F6ulVGrISgTVrzsV0jUePTBnOt/Gd+adR6FCn8CmG8z5Zk9cnzjOM5wAcd/WWX0lnt9ZiUaj4orDpH4x9JrNrVSBhdRrtTU47AAH3xKl1SwvVsVval5UYVyhNLU+NL7oc6sA8HAUDfE6cvsNWqqqWYhQoJLMQAAOSSeBIfT+s21ditGtTqFRkhGDEDjOB6e8+beLL1/wXTLcamSrQos6r89TQlIKo7klj33x2krw10mt/aFGvTsntaCo6uHYtq8jgE6sNkkptg/LmB9QiIgIiICIiAiIgIiIHmZAv8AqlCkypUqKr1CAik+ZiTgaVG53OJRPHNq1neUepUwSpdVqgd8YI/zpkdgVB5M2+HB+P6lVvTvRt8JRyOTjCnf2LNg7guvaBbLygdQ+p/MYkVQdZP9zb7nf90r3hXrNxdWt49aoWamraCAqaf+mx20geoG85nRKzv0q5d3d203A1Oxdv8A41PLHMDqX9yiOS7quWIGpgM4ONsyHV6vQR/htUUOSBjc4J4BIGB9zKxT6Ch6c92S+tagVBto06whGMZzkk89pt6/0elS6fa10B11iC7EnJ1oWxjjAK7Tnui6W7qfXKdolLWrnXrICAHcEZLZI9GH7Zyk8dqWYCg5JGEw3mZj8oK42B9s/ebf0kUF12eB87vqHod6WdvfJmrrFEDqtqo28qDccYd5xlccpy7x3PDoeFvEtavXa3r01puqMylQysuCMq4YnOzZztxMeh+Iq4W+S5YM9qrOuFVPk1qwAA41BcZz88573SW/Wn1hsP8ADprpA+aolNVO5G2eTNX6QbB0uVant+NQUyB/3MroCNu//T/YZzJN615i23X8LR4C+KbUVKzu7VnZgajFiFHlUDPAOkn/ADTj+If/ANm0x/46X+5Wl4s7QUqdOmvFNFQfRQB+6VvrHQ6r9QoXQKBKSICCTrJV6hOAFxjDjfPeZzLm2rZxJHFqWVOv1p0qoGQIraW4JWkmAR6jfj2jwdYUhf3qaFKoXRARkKpqEEDPsAJ2R0Y/jnvNfzoFCBePIq515/u9vWSOj9Lp29arWUuWrsS2ojSMsWwoAzyfeXLPjX4izC+fyonhNC9pc00Iao6OQgPnK/DHmA7Z2+pmmx64i2T22li7BwNIyCGOosT7DP7J9N6V4ftbd2qUaYRnBBOpjgE5IXJwBkDYdhNV50mkjGoiIus+YqoDEnuwGTOserLU7bIrvheh+O6U9moKvSbKu3yszVWqqAR6Ywp+s4/X7PqVGyWncuiUKbIiU8qzsRnTgryqgE7n0G3b6PZEVKT0CShdGTUuNQ1JpyNsZA4+k4tj+jigrq1WrUrKnyo+Am3o3JI9gQD6zfG7jKzVL7wq13Y2QV/h17ehR0sc43ppqUkbg5QEEcY95N8P+H7ynWFe6u2qsqsionyYbGdRIHYHZQcgbniW6JUIiICIiAiIgIiICIiBwvGlNWsbkMAQKDsM+jINSn6ggH7Tm/oxUDp9MgDzPWJI9T8Rhk/YAfaWmtSV1KsoZWBDKwBUg8gg7ERQoIihUVUUcKoCgfQDaB8h6Ib62/E2VO1Z3rkprYMqpsylskaSpByCSB9eJ1fDHR738Fc2z0NAam/wy+FZnddJU+b5Rgb49eTPp8QKBaeGardM/BuyI5csW3dQPi6/QDJwJIv/AAstW0o2ruQaATDoBuVUqfKfQg95abijp8wPPpNQIIwZ5+r3S8Vrjq+VfHhO3NOhTcu4ti5QltJJdgxLacZ3AnVr9MoPVWu1NTUQYVyNxjJGP2neZVwwV9LBTobSzfKDg4LewPM5Xh2s6Wzvc3KVyjOzPTIZUVVBK5UDJG54/wC6Ybys5rTUjsG1UsHwpYDAbA1Af4ucSs2HhWubhbi6riqaRY0kAOFJOQTxxz9QN9plc+OrFANLu+r0RCMb4ydenH+s6d91ulStvxWrUhVSgXYuX+QAHg7754we0smU9eUtl9uuurtBJ4PB7z5ze+PL5KQqC2VEc+So4d0IwTgbrk+oPYHYz6EtZioOMkqPbkZlyxskJd1Vet+MLe2c0grVHXZgmAqn9UsTu3sAcTo9F6st1QFZEZBrKgNg504yQR6ZOPqDKVbVbvpteu72xdKjEl8NjSGZsh1BAzqyQew7Tr9a8SLW6c9aiGRnqLScH5kJ3bBHdfUfrd51enONT72kz+b9LHR61ba/hrWps5ONAdSSew359pl1/rNC2paqxPnyFRQC7HG+kZxttuSANpQfEPhyhb2FCuhIqsaZZtRw2tCxwOBggYx2k3rNwH6hYm4xo/D0mOv5dbayc52+cJn6CMenJdy/KXO13vCviK2uahSn8RH05AqafMF5KlSdx2P574iXnjm7atWt7a2V3pO6g5Z/KjFWYqNPttnk+shBkqdapNR0kKhNQpjTkI4bJGx2ZF/KS/A//wB/qH+Nv915rjdTcc3m6rr+CfEtW8ou1QKHR9JKDCsCAQcEnB5H2lrovnIM+Vfo86p8L8TRFN3qBalUKvBNJSNB9QxYgDbvLl4S6lcXFA1K9II/xGVQFZAygKQ2lyTySM530yXumVvpJqzS0BhMpEpuAd8CShNMcu6bc2aexETtCIiAiIgIiIHM691VbW3qV2GQg2HGpiQEXPuSBmfOXodXuaDX34h0UK1RKNJnQsq/qqux2GwbJb7yz/pRQmxYjhatMt9NWP8A2KyZ4e63bCxo1GqoipRRXywGlkUKykc5yOOTtjmBFfxQ9t0+ncXSN8dho+Gw0M7AtgkY8oKrqO22eOBOb0zx1cC4p0ru2+CtcqEbDKRqOFJDcjJAPGM5kL9IF+tanYXaAvR+IzHbfOUbQw/WwjjHcGa+v9Tp9SvrKnbZcUnL1HKsoCl0Z/mAPlCc8ZYCBt671e/qdQe0t6ioulcalXCA01Z2LaSc7n9s4vTaF9dPWs3unUUWYuSWfUytoC5yCUJ33OPad1aDf23VOltIpgFgDpGaCevE2eGbCrTvryo6MqOz6HYYD5qE+XuMb5mOV1u/7bTGbRfAd272NyjsSE16NRzgNTyQCfTOTj3Mw8JKP7Juu+m5/wBlZs8JeHbuj8Wm5RaLo42IZmc4VWGNwNOrY49JN8PeFKtClXovcKyVqboFQNhC40l8NjfGNvbmc247v061eFatOnUv7Hq1tCmp8QecgFxiqigK3IGM7Due839UQ1Oj0SjBvgspqBTqKDzjzAcY1A/TeXGy8N0ktjaMzOjaixOFbzMG2xxggEfSaU6R+Dt6qWiFnbLKHbVqfAAzqIGMem3E4uc39rMb/SheJvEqXNrSpJTZfhFdbHGgMKbKFUjuMnfGw47fWrWmdK/4V/0H8JRH6N1C+NNLmmlCgj62CaQW2wdIDMdWCR6AZJ3n0BlIPG3pj0jqSSTSY73VK6j1bqxerRS0BVndUfTnyEkKSdejOnB3+4knpvgwLYPbVGw9RviMy+YI4xoA4yAFAPfJlu14ngqZk/6zWpwvb8qDZeBrhmRLm410KR8lNCzAgcL5saR6eu2wxLH4h8N0btVD5DJnSy7MAcZXjGNuMTuqIzmS5287WYyK70DoFK0J+Gpy2NTsdTkD0B4A9gJ27SzoIzvTpIjucu6qFZySTlmAydyT95sZSIpuBz6zjHPLu5W4yzhvCDnAGecDGfrEyzmeaZvfw4DtJFM7CR9Im6idv3Tvp+XGXhuiImzgiIgIiICIiBourZKiMjqGV1Ksp4IPIlMp/oxsg+stVZc50FlC/QsFDY++feXqIEJum0TS+AaaGkFC/DKgpgcDTxMendJt7cEUaSU9XOhQpPbJ5MnxAxIkGrQI43H9cSfElks1Vl14ckgehmDPnZgPb+U6b26mQ61mfrMMujZ+1rj1J7QTQYb5/ObFz3m1UIO/EJSHEwyxsurGsylYWdzuUPIzj3HtJwInJpW3mOScgmT6FUHynkfnOpdeHOU9txUGa2p4mzExBkyxl8pLWKz0AczxhPVnE44dPDtMXQMpHBmxTPCyiJjztNvKbYAB2I2m3Mh10823qBJFJsDB9Jrjl6Sz2247zOiu+e006/cSRb8HtNcJLfDPLw3xETdmREQEREBERAREQEREBERAREQI90vl+kiLnMn1BkGQURjtiY9XG2yx3hlJvbCouGz3mNZOGH3mxgSB3BnoHofUTz2c2VtLxt5Tc433x6zJ9+DPE2mJpgcHGYu7NHG2QUzIJ2mIqY7GZGr2EuPRc3J6J4y5E8yx5EzW3YjtLOllvXpO6I4GefSSqNDIBJnlK1PrJYGJr0ulcbuuc898RrFuvabAMTKJuzIiICIiAiIgIiICIiAiIgIiICIiAnk9iBDrUDnK+s1tTZd+RJ8Tm4427sWZWIlOhkb8Tatuo9JuiWYyTULdsBTHaZBR2mUSo8nsRAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQP/Z', max_length=10000),
        ),
    ]
