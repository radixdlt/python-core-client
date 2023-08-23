import urllib.request, logging, subprocess, os, shutil

logger = logging.getLogger()
logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', level=logging.INFO)

SPEC_URL_BRANCH_PLACEHOLDER='[branch]'
CORE_SPEC_URL='https://raw.githubusercontent.com/radixdlt/babylon-node/' + SPEC_URL_BRANCH_PLACEHOLDER + '/core-rust/core-api-server/core-api-schema.yaml'
OPENAPI_GENERATION_FOLDER='.'
OPENAPI_GENERATOR_FIXED_VERSION_JAR=os.path.join(OPENAPI_GENERATION_FOLDER, 'openapi-generator-cli-5.2.1.jar')
OPENAPI_GENERATOR_FIXED_VERSION_DOWNLOAD_URL='https://search.maven.org/remotecontent?filepath=org/openapitools/openapi-generator-cli/5.2.1/openapi-generator-cli-5.2.1.jar'

def safe_os_remove(path, silent = False):
    try:
        shutil.rmtree(path) if os.path.isdir(path) else os.remove(path)
    except Exception as e:
        if not silent: logger.warning(e)

def replace_in_file(filename, target, replacement):
    with open(filename, 'r') as file:
        file_contents = file.read()
    file_contents = file_contents.replace(target, replacement)
    with open(filename, 'w') as file:
        file.write(str(file_contents))

def run(command, cwd = '.', should_log = False):
    if (should_log): logging.debug('Running cmd: %s' % command)
    response = subprocess.run(' '.join(command), cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stderr = response.stderr.decode('utf-8')
    if response.returncode != 0: raise Exception(stderr)
    stdout = response.stdout.decode('utf-8')
    if (should_log): logging.debug('Response: %s', stdout)
    return stdout

def generate_client(spec_file, package_name, client_fix_hack=lambda: None):
    tmp_client_folder = '%s.tmp' % package_name
    safe_os_remove(package_name, True)
    # generate the full package
    run(['java', '-jar', OPENAPI_GENERATOR_FIXED_VERSION_JAR, 'generate',
         '-g', 'python',
         '-i', spec_file,
         '-o', '../',
         '--additional-properties=packageName=%s' % package_name,
         '-t', os.path.join(OPENAPI_GENERATION_FOLDER, '5.2.1-template-file-overrides')
         ], should_log=False)
    logging.info("Succesfully generated client in package '%s.'" % package_name)


def get_branch_names_from_env_variables():
    return (
        os.environ.get('RADIXDLT_GATEWAY_API_SPEC_BRANCH', 'main'),
        os.environ.get('RADIXDLT_CORE_API_SPEC_BRANCH', 'main'),
        os.environ.get('RADIXDLT_SYSTEM_API_SPEC_BRANCH', 'main')
    )

if __name__ == "__main__":
    # check & download the openapi-generator.jar
    if not os.path.exists(OPENAPI_GENERATOR_FIXED_VERSION_JAR):
        logger.info('%s does not exist' % OPENAPI_GENERATOR_FIXED_VERSION_JAR)
        logger.info('Will download it from %s...' % OPENAPI_GENERATOR_FIXED_VERSION_DOWNLOAD_URL)
        urllib.request.urlretrieve(OPENAPI_GENERATOR_FIXED_VERSION_DOWNLOAD_URL, OPENAPI_GENERATOR_FIXED_VERSION_JAR)
        logger.info('Testing the openapi-generator...')
        run(['java', '-jar', OPENAPI_GENERATOR_FIXED_VERSION_JAR, 'author'], should_log=False)
        logger.info('All good.')

    # download & fix the spec files
    core_api_spec_filename = os.path.join(OPENAPI_GENERATION_FOLDER, 'core_api_spec.yaml')
    core_api_branch = os.getenv("CORE_API_BRANCH", "main")
    urllib.request.urlretrieve(CORE_SPEC_URL.replace(SPEC_URL_BRANCH_PLACEHOLDER, core_api_branch), core_api_spec_filename)
    replace_in_file(core_api_spec_filename, 'openapi: 3.1.0', 'openapi: 3.0.0')
    # generate the clients
    logging.info('Downloaded all 3 OpenAPI specs. Generating clients...')
    generate_client(core_api_spec_filename, "core_client")
    logging.info("All 3 clients have been created.")


    os.remove("core_api_spec.yaml")
    os.remove("openapi-generator-cli-5.2.1.jar")