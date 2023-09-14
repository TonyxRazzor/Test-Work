from pyspark.sql.functions import explode


def get_products_categories(df):
    # разбиваем колонку с категориями на отдельные строки
    df = df.select("product", explode("categories").alias("category"))
    # объединяем продукты без категорий
    df_no_category = df.filter("category is null").select("product", "category")
    # удаляем продукты без категорий из основного датафрейма
    df = df.filter("category is not null")
    # возвращаем объединенный датафрейм
    return df.union(df_no_category)
