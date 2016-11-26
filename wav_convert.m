BASE_PATH = '/Volumes/CAR MUSIC';
DEST_PATH = strcat(BASE_PATH, 'MP3 files');
%cd '/Volumes/CAR\ MUSIC/'; %% TODO: replace with argument
system('echo $(find -H . -name *m4a) > files.txt');

files = fopen('files.txt');
paths = strsplit(fgetl(files), '.m4a');

for i = 1:length(paths)
        filename = char(paths(i));
        filename = regexprep(filename, '[^a-zA-Z0-9\/\s]', '');
        fprintf('[%d]: %s\n', i, filename);
        [y, fs] = audioread(strcat(BASE_PATH, filename, '.m4a'));
        filename = regexprep(filename, '/', '-'); 
        audiowrite(strcat(DEST_PATH, filename,'.wav'), y, fs, 'BitsPerSample', 32);
end