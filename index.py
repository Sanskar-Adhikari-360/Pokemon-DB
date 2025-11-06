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
    Id, Name, Type1, Type2, Hp, Attack, Defense, speed, Sp_attack, Sp_defense ,Weight, Height, Ability, image, Dex_entry = p

    content = f"""
    <body class = "type_{Type1}">
    <main class ="detail-main">    
    <header class="header">
        <div class="header-wrapper">
          <div class="header-wrap">
            <a href="index.html" class="back-btn-wrap">
              <img src="/assets/Ui/back-to-home.svg" alt="back to home" class="back-btn" id="back-btn">
            </a>
            <div class="name-wrap">
              <h1 class="name">{Name}</h1>
            </div>
          </div>
          <div class="pokemon-id-wrap">
            <p class="body2-fonts">#{Id}</p>
          </div>
        </div>
      </header>
      
      <div class="featured-img">
        <a href="{Id - 1}.html" class="arrow left-arrow" id="leftArrow">
          <img src="/assets/Ui/chevron_left.svg" alt="back">
        </a>
        <div class="detail-img-wrapper">
          <img src="{image}" alt="venusaur">
        </div>
        <a href="{Id + 1}.html" class="arrow right-arrow" id="rightArrow">
          <img src="/assets/Ui/chevron_right.svg" alt="forward">
        </a>
      </div>
      
      
      <div class="detail-card-detail-wrapper">
        <div class="power-wrapper"><p class="body3-fonts" style = "background-color: var(--{Type1});">{Type1}</p><p class="body3-fonts" style = "background-color: var(--{Type1});">{Type2}</p></div>
        <p class="body2-fonts about-text">About</p>
        <div class="pokemon-detail-wrapper">
          <div class="pokemon-detail-wrap">
            <div class="pokemon-detail">
              <img src="/assets/Ui/weight.svg" alt="weight">
              <p class="body3-fonts weight">{Weight}</p>
            </div>
            <p class="caption-fonts">Weight</p>
          </div>
          <div class="pokemon-detail-wrap">
            <div class="pokemon-detail">
              <img src="/assets/Ui/height.svg" alt="height" class="straighten">
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
         <div class="stats-wrapper">
        <div class="stats-wrap">
          <p class="body3-fonts stats" style="color: var(--{Type1});">HP</p>
          <p class="body3-fonts">{Hp}</p>
          <progress class="progress-bar" value="{Hp}" max="100" style="color: var(--{Type1});"></progress>
        </div>
        <div class="stats-wrap">
          <p class="body3-fonts stats" style="color: var(--{Type1});">ATK</p>
          <p class="body3-fonts">{Attack}</p><progress class="progress-bar" value="{Attack}" max="100"
            style="color: var(--{Type1});"></progress>
        </div>
        <div class="stats-wrap">
          <p class="body3-fonts stats" style="color: var(--{Type1});">DEF</p>
          <p class="body3-fonts">{Defense}</p><progress class="progress-bar" value="{Defense}" max="100"
            style="color: var(--{Type1});"></progress>
        </div>
                        <div class="stats-wrap">
          <p class="body3-fonts stats" style="color: var(--{Type1});">SATK</p>
          <p class="body3-fonts">{Sp_attack}</p><progress class="progress-bar" value="{Sp_attack}" max="100"
            style="color: var(--{Type1});"></progress>
        </div>
                <div class="stats-wrap">
          <p class="body3-fonts stats" style="color: var(--{Type1});">SDEF</p>
          <p class="body3-fonts">{Sp_defense}</p><progress class="progress-bar" value="{Sp_defense}" max="100"
            style="color: var(--{Type1});"></progress>
        </div>
               <div class="stats-wrap">
          <p class="body3-fonts stats" style="color: var(--{Type1});">SPD</p>
          <p class="body3-fonts">{speed}</p><progress class="progress-bar" value="{speed}" max="100"
            style="color: var(--{Type1});"></progress>
        </div>

    <img src="/assets/Ui/pokedex.svg" alt="pokedex" class="detail-bg">
    </main>
    """

    with open(f"pokedex_pages/{Id}.html", "w", encoding="utf-8") as f:
        f.write(header.format(title=Name) + content + footer)

# Generate index.html
index_content = header.format(title="Pokédex") + """
<body>
    <main class="main">
      <header class="header home">
        <div class="container">
          <div class="logo-wrapper">
            <img src="/assets/Ui/pokeball.svg" alt="pokeball" />
            <h1>Pokedex</h1>
          </div>
          <div class="search-wrapper">
            <div class="search-wrap">
              <img
                src="/assets/Ui/search.svg"
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
                src="./assets/Ui/cross.svg"
                alt="cross icon"
                class="search-close-icon"
                id="search-close-icon"
              />
            </div>
            <div class="sort-wrapper">
              <div class="sort-wrap">
                <img
                  src="/assets/Ui/sorting.svg"
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
    Id, Name, Type1, Type2, Hp, Attack, Defense, speed, Sp_attack, Sp_defense ,Weight, Height, Ability, image, Dex_entry = p

    index_content += f"""
        <a href='{Id}.html'>
          <div class="list-item">
            <div class="number-wrap">
              <p class="caption-fonts">{Id}</p>
            </div>
            <div class="img-wrap">
              <img src = "{image}">
            </div>
            <div class="name-wrap">
              <p class="body3-fonts">{Name}</p>
            </div> 
            
          </div>
          </a>
    """

index_content += index_footer

with open("pokedex_pages/index.html", "w", encoding="utf-8") as f:
    f.write(index_content)

print("✅ Pokédex website generated successfully!")
