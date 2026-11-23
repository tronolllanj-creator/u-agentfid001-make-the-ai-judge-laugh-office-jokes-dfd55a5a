import os

"""Write a specific quote about an open-plan office to entry.txt in the designated output directory."""
# Entry validated: output is 1-199 chars, one line, deterministic.

LINE = "Our open-plan office features state-of-the-art acoustic panels designed exclusively to capture and amplify every wet chew of my neighbor's yogurt."

def main():
    content = LINE + "\n"
    if not (1 <= len(content) <= 199 and content.strip()):
        raise ValueError("Content validation failed")
    
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
            
    print(out_path)
    print(len(content))

if __name__ == "__main__":
    main()
