# IVS Projekt 2 - Týmová implementace kalkulačky

Tento projekt byl vytvořen jako druhý projekt do předmětu IVS (Praktické aspekty vývoje software). Cílem bylo vytvořit matematickou kalkulačku obsahující matematickou knihovnu, grafické uživatelské rozhraní (GUI) a automatizované testy.

## Autorský tým

| Jméno a příjmení | Login (GitHub) | Role v projektu / Co implementoval |
| :--- | :--- | :--- |
| **Marek Janiga** | `xjanigm00` (`hajtik1`) | Matematická knihovna, testy knihoven |
| **Daniel Forman** | `xformad01` (`danielf40k`) | GUI aplikace (Flet), Main |
| **Simona Studená** | `xstudes00` (`simisekstudena-bit`) | Matematická logika, makefile, testy mat. logiky |
| **Josef Jindra** | `xjindrj00` (`pepekherni-ctrl`) | GUI bugfix, nápověda, instalátor, dokumentace |

## Technologie
* **Jazyk:** Python 3
* **GUI Framework:** Flet
* **Testování:** `unittest` / `pytest`
* **Sestavení a správa:** GNU Make

## Sestavení a spuštění (Návod k použití)

Projekt využívá nástroj `make` pro automatizaci běžných úloh. V kořenovém adresáři repozitáře lze spustit následující příkazy:

### `make install`
Nainstaluje všechny potřebné závislosti (především framework Flet) nezbytné pro běh aplikace. 

### `make run`
Spustí samotnou aplikaci kalkulačky s grafickým rozhraním.

### `make test`
Spustí sadu automatizovaných testů pro ověření správné funkčnosti matematické knihovny.

### `make doc`
Vygeneruje vývojářskou dokumentaci zdrojového kódu (Doxygen) do složky `doc/`.

### `make pack`
Zabalí celý repozitář do `.zip` archivu ve formátu požadovaném pro finální odevzdání projektu.

### `make clean`
Odstraní všechny dočasné soubory, meziprodukty překladu, vygenerovanou dokumentaci a instalační archivy.

## Struktura repozitáře
* `src/` - Zdrojové kódy aplikace, matematické knihovny a grafického rozhraní.
* `tests/` - Skripty s automatizovanými testy matematické knihovny.
* `doc/` - Uživatelský manuál a technická dokumentace.
* `Makefile` - Skript definující cíle pro sestavení, spuštění a testování projektu.