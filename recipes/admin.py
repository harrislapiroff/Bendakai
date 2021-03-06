from django.contrib import admin
from .models import Ingredient, MeasurementUnit, Recipe, RecipeIngredient, JunkRecipe, Photo, UserRecipeRating, UserIngredientRating, PantryItem, KitchenTool, UserSavedRecipe, UserKitchenTool
from reversion.admin import VersionAdmin

class RecipeIngredientInline(admin.StackedInline):
	model = RecipeIngredient

class RecipeAdmin(VersionAdmin):
	inlines = (RecipeIngredientInline, )

admin.site.register((Ingredient, MeasurementUnit, RecipeIngredient, JunkRecipe, Photo, UserRecipeRating, UserIngredientRating, PantryItem, UserKitchenTool, KitchenTool, UserSavedRecipe), VersionAdmin)
admin.site.register(Recipe, RecipeAdmin)