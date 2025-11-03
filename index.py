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

# Write CSS and JS files if they don’t exist
if not os.path.exists("pokedex_pages/style.css"):
    with open("pokedex_pages/style.css", "w", encoding="utf-8") as f:
        f.write("""/* (Paste the CSS code here) */""")

if not os.path.exists("pokedex_pages/script.js"):
    with open("pokedex_pages/script.js", "w", encoding="utf-8") as f:
        f.write("""/* (Paste the JS code here) */""")

# HTML header and footer templates
header = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
"""

footer = """
<script src="script.js"></script>
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
    Id, Name, Type1, Type2, Hp, Attack, Defense, speed,image = p

    content = f"""
    <div class="card">
        <h1>{Name}</h1>
        <p><strong>Type 1:</strong> {Type1}</p>
        <p><strong>Type 2:</strong> {Type2}</p>
        <p><strong>Hp:</strong> {Hp}</p>
        <p><strong>Attack:</strong> {Attack}</p>
        <p><strong>Defense:</strong> {Defense}</p>
        <a href="index.html">← Back to Pokédex</a>
        <img src = {image}/>
    </div>
    """

    with open(f"pokedex_pages/{Name.lower()}.html", "w", encoding="utf-8") as f:
        f.write(header.format(title=Name) + content + footer)

# Generate index.html
index_content = header.format(title="Pokédex") + """
    <main class="main">
      <header class="header home">
        <div class="container">
          <div class="logo-wrapper">
            <img src="./assets/pokeball.svg" alt="pokeball" />
            <h1>Pokedex</h1>
          </div>
          <div class="search-wrapper">
            <div class="search-wrap">
              <img
                src="./assets/search.svg"
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
                  src="./assets/sorting.svg"
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
    index_content += f"""
    <div class="list-item">
        <h2><a href='{Name.lower()}.html'>{Name}</a></h2>
    </div>
    """

index_content += index_footer

with open("pokedex_pages/index.html", "w", encoding="utf-8") as f:
    f.write(index_content)

print("✅ Pokédex website generated successfully!")
