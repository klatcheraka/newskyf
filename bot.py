import sys
import pkg_resources

print("Python executable:", sys.executable)
installed_packages = [p.key for p in pkg_resources.working_set]
print("Installed packages:", installed_packages)

from dotenv import load_dotenv
load_dotenv()
