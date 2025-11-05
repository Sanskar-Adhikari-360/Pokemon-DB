import sqlite3
import os

# Connect to database
conn = sqlite3.connect("PokemonDB.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM Pokemon")
Pokemon = cursor.fetchall()
conn.close()

# Create folder if it doesn’t exist
os.makedirs("pokedex_pages", exist_ok=True)

# # Write CSS and JS files if they don’t exist
# if not os.path.exists("pokedex_pages/style.css"):
#     with open("pokedex_pages/style.css", "w", encoding="utf-8") as f:
#         f.write("""/* (Paste the CSS code here) */""")

# if not os.path.exists("pokedex_pages/script.js"):
#     with open("pokedex_pages/script.js", "w", encoding="utf-8") as f:
#         f.write("""/* (Paste the JS code here) */""")

# HTML header and footer templates
header = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
</head>
"""

footer = """
</body>
</html>
"""
index_footer = """
        
        </div>
        </div>
        <div id="not-found-message">Pokemon not found</div>
      </section>
    </main>
  </body>
</html>
"""

# Generate a page for each Pokémon
for p in Pokemon:
    Id, Name, Type1, Type2, Hp, Attack, Defense, speed,  Weight, Height, Ability, image, Dex_entry = p

    content = f"""
    <body class = "type_{Type1}">
    <main class ="detail-main">    
    <header class="header">
        <div class="header-wrapper">
          <div class="header-wrap">
            <a href="index.html" class="back-btn-wrap">
              <img src="/assets/back-to-home.svg" alt="back to home" class="back-btn" id="back-btn">
            </a>
            <div class="name-wrap">
              <h1 class="name">{Name}</h1>
            </div>
          </div>
          <div class="pokemon-id-wrap">
            <p class="body2-fonts">#001</p>
          </div>
        </div>
      </header>
      
      <div class="featured-img">
        <a href="#" class="arrow left-arrow" id="leftArrow">
          <img src="/assets/chevron_left.svg" alt="back">
        </a>
        <div class="detail-img-wrapper">
          <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/3.svg" alt="venusaur">
        </div>
        <a href="#" class="arrow right-arrow" id="rightArrow">
          <img src="/assets/chevron_right.svg" alt="forward">
        </a>
      </div>
      
      
      <div class="detail-card-detail-wrapper">
        <div class="power-wrapper"><p class="body3-fonts type grass">grass</p><p class="body3-fonts type poison">poison</p></div>
        <p class="body2-fonts about-text">About</p>
        <div class="pokemon-detail-wrapper">
          <div class="pokemon-detail-wrap">
            <div class="pokemon-detail">
              <img src="/assets/weight.svg" alt="weight">
              <p class="body3-fonts weight">{Weight}</p>
            </div>
            <p class="caption-fonts">Weight</p>
          </div>
          <div class="pokemon-detail-wrap">
            <div class="pokemon-detail">
              <img src="/assets/height.svg" alt="height" class="straighten">
              <p class="body3-fonts height">{Height}</p>
            </div>
            <p class="caption-fonts">Height</p>
          </div>
          <div class="pokemon-detail-wrap">
            <div class="pokemon-detail move"><p class="body3-fonts">{Ability}</p></div>
            <p class="caption-fonts">Ability</p>
          </div>
        </div>
        <p class="body3-fonts pokemon-description">{Dex_entry}</p>
        <p class="body2-fonts about-text">Base Stats</p>
        <div class="stats-wrapper"><div class="stats-wrap">
        <p class="body3-fonts stats" style="color: rgb(120, 200, 80);">HP</p>
        <p class="body3-fonts">{Hp}</p>
        <progress class="progress-bar" value="{Hp}" max="100" style="color: rgb(120, 200, 80);"></progress></div><div class="stats-wrap"><p class="body3-fonts stats" style="color: rgb(120, 200, 80);">ATK</p><p class="body3-fonts">{Attack}</p><progress class="progress-bar" value="{Attack}" max="100" style="color: rgb(120, 200, 80);"></progress></div><div class="stats-wrap"><p class="body3-fonts stats" style="color: rgb(120, 200, 80);">DEF</p><p class="body3-fonts">{Defense}</p><progress class="progress-bar" value="{Defense}" max="100" style="color: rgb(120, 200, 80);"></progress></div><div class="stats-wrap"><p class="body3-fonts stats" style="color: rgb(120, 200, 80);">SPD</p><p class="body3-fonts">{speed}</p><progress class="progress-bar" value="{speed}" max="100" style="color: rgb(120, 200, 80);"></progress></div></div>
      </div>    
    <img src="/assets/pokedex.svg" alt="pokedex" class="detail-bg">
    
    <!--
    <div class="card">
        <img src = {image}/>
        <h1>{Name}</h1>
        <p><strong>Type 1:</strong> {Type1}</p>
        <p><strong>Type 2:</strong> {Type2}</p>
        <p><strong>Hp:</strong> {Hp}</p>
        <p><strong>Attack:</strong> {Attack}</p>
        <p><strong>Defense:</strong> {Defense}</p>
        <a href="index.html">← Back to Pokédex</a>
        </header>
        </div>
        -->
    </main>
    """

    with open(f"pokedex_pages/{Name.lower()}.html", "w", encoding="utf-8") as f:
        f.write(header.format(title=Name) + content + footer)

# Generate index.html
index_content = header.format(title="Pokédex") + """
<body>
    <main class="main">
      <header class="header home">
        <div class="container">
          <div class="logo-wrapper">
            <img src="/assets/pokeball.svg" alt="pokeball" />
            <h1>Pokedex</h1>
          </div>
          <div class="search-wrapper">
            <div class="search-wrap">
              <img
                src="/assets/search.svg"
                alt="search icon"
                class="search-icon"
              />
              <input
                type="text"
                class="search-input body3-fonts"
                placeholder="Search"
                id="search-input"
              />
              <img
                src="./assets/cross.svg"
                alt="cross icon"
                class="search-close-icon"
                id="search-close-icon"
              />
            </div>
            <div class="sort-wrapper">
              <div class="sort-wrap">
                <img
                  src="/assets/sorting.svg"
                  alt="sorting"
                  class="sort-icon"
                  id="sort-icon"
                />
              </div>
              <div class="filter-wrapper">
                <p class="body2-fonts">Sort by:</p>
                <div class="filter-wrap">
                  <div>
                    <input
                      type="radio"
                      id="number"
                      name="filters"
                      value="number"
                      checked
                    />
                    <label for="number" class="body3-fonts">Number</label>
                  </div>
                  <div>
                    <input type="radio" id="name" name="filters" value="name" />
                    <label for="name" class="body3-fonts">Name</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>
      <section class="pokemon-list">
        <div class="container">
          <div class="list-wrapper">
"""

for p in Pokemon:
    Name = p[1]
    Id = p[0]
    index_content += f"""
          <div class="list-item">
            <div class="number-wrap">
              <p class="caption-fonts">{Id}</p>
            </div>
            <div class="img-wrap">
              <img>
            </div>
            <div class="name-wrap">
              <p class="body3-fonts"><a href='{Name.lower()}.html'>{Name}</a></p>
            </div> 
            
          </div>
    """

index_content += index_footer

with open("pokedex_pages/index.html", "w", encoding="utf-8") as f:
    f.write(index_content)

print("✅ Pokédex website generated successfully!")
