if __name__ == '__main__':
    for i in range(10):
        title="%d.txt"%i
        try:
            with open("source_dir/"+title,'w') as file:
                file.write(title)
        except Exception as e:
            print(e)
        finally:
            file.close()