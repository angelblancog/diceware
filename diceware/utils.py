from pathlib import Path


def load_words(
    path: Path,
    encoding: str = "utf-8",
    line_separator: str = "\n",
    pair_separator: str = "\t"
    ) -> dict[str, str]:
    
    contents = path.read_text(encoding=encoding).split(line_separator)
    
    # Remove last empty string
    pairs = [pair for pair in contents if pair]
    
    # Create the dictionary
    return {
        pair.split(pair_separator)[0]: pair.split(pair_separator)[1]
            for pair in pairs
    }
   
