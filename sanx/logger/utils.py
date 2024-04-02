import asyncio
from io import TextIOWrapper
from pathlib import Path

# Global flag to signal the program to stop
stop_flag = False

async def get_file_reader(thefile: TextIOWrapper):
    thefile.seek(0, 2) # Go to the end of the file
    while True:
        line = thefile.readline()
        if not str(line).strip():
            await asyncio.sleep(0.1) # Sleep briefly
            continue
        yield line

async def send_lines_to_ui(file_path: Path):    
    global stop_flag 
    with open(file_path, "r") as file:
        line_generator = get_file_reader(file)
        async for line in line_generator:
            if stop_flag:
                break
            # do whatever you want with line here
            await write_lines_to_ui(str(line).strip())

async def write_lines_to_ui(line: str):
    print(line)
    await asyncio.sleep(0)
    
def send_stop_signal():
    global stop_flag
    stop_flag = True

if __name__ == "__main__":
    log_folder = Path(__file__).parent
    asyncio.run(send_lines_to_ui(log_folder / "t.log"))

