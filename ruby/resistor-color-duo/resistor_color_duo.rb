module ResistorColorDuo
 COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

  def self.value(color_array)
      color_array.reverse!
      numlist = color_array.map.with_index {|n,i| COLORS.index(n)*(10**i)}

      return numlist.reduce(:+)
  end

end

